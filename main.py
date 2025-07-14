import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    args = sys.argv
    if len(args) == 1: 
        print("No arguments given. Enter a prompt to get a response.")
        exit(1)

    client = genai.Client(api_key=api_key)
    res = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=args[1])

    print(res.text)
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
