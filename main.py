import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    # Get prompt arguments and return error if empty or more than 2
    args = sys.argv
    if len(args) == 1: 
        print("No arguments given. Enter a prompt to get a response.")
        exit(1)
    elif len(args) > 3:
        print(f"Too many arguments given. Program expects at most 2 parameters, but was given {len(args) - 1}")
        exit(1)
    elif args[1] == "--verbose":
        print("Optional flag 'verbose' should be set last.")
        print("Enter command as:\n")
        print("'uv run main.py <prompt> <flag>'\n")
        exit(1)

    # Check if 'verbose' flag is set
    is_verbose = True if sys.argv[-1] == "--verbose" else False
    
    # Store prompt in content list to track conversation
    user_prompt = args[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Send content list to AI API and store response
    client = genai.Client(api_key=api_key)
    res = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages)

    # Print response (and optionally additional prompt data)
    print(res.text)

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
