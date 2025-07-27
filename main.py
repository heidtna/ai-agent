import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT, MAX_ITERATIONS
from functions.declarations import available_functions
from functions.call_function import call_function

def main():
    load_dotenv()

    # Get prompt arguments and return error if empty or more than 2
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    # Check if 'verbose' flag is set
    is_verbose = "--verbose" in sys.argv

    user_prompt = " ".join(args)

    if is_verbose:
        print("User Prompt: ", user_prompt)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Send content list to AI API and store response
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    iterations = 0
    while True:
        iterations += 1
        
        if iterations > MAX_ITERATIONS:
            print(f"Maximum number of {MAX_ITERATIONS} reached. Terminating program.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, is_verbose)

            if final_response:
                print("\n*** Final Response ***\n", final_response)
                break
        except Exception as e:
            print(f"Error: Content generation failed.\n  <{e}>")    

def generate_content(client, messages, is_verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT)
    )

    if is_verbose:
        print(f"\tPrompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"\tResponse tokens: {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            function_content = candidate.content
            messages.append(function_content)

    # End conversation when program no longer needs to make specific function calls
    if not response.function_calls:
        return response.text
    
    function_call_responses = []
    for function_call in response.function_calls:
        try:
            function_call_result = call_function(function_call, is_verbose)
            function_call_response = function_call_result.parts[0].function_response.response

            if is_verbose:
                print(f"--> Function call results:\n{function_call_response["result"]}")

            function_call_responses.append(function_call_result.parts[0])

        except Exception as e:
            print(f"Error: Calling function '{function_call.name}' failed.\n  <{e}>")

    if not function_call_responses:
        raise Exception("No function response generated, exiting.")
    
    messages.append(types.Content(role="tool", parts=function_call_responses))
        

if __name__ == "__main__":
    main()
