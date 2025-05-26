# agent.py
# This file defines a simple AI agent function and a command-line interface for it.

import os

def run_ai_agent(api_key: str, prompt: str) -> str:
    """
    Simulates an AI agent processing a prompt using an API key.

    Args:
        api_key: The API key for the AI service.
        prompt: The prompt to send to the AI.

    Returns:
        A string representing the AI's response or an error message.
    """
    if not api_key:
        return "Error: API key not provided."

    # Simulate using the API key by including parts of it in the response.
    # For security, only show the first 4 and last 4 characters.
    if len(api_key) > 8:
        displayed_key = f"{api_key[:4]}...{api_key[-4:]}"
    else:
        displayed_key = api_key # Or some other placeholder if key is too short

    return f"AI (using key '{displayed_key}'): Processed '{prompt}'"

if __name__ == "__main__":
    # Attempt to read the API key from an environment variable.
    api_key = os.environ.get("GOOGLE_API_KEY")

    if not api_key:
        print("Warning: GOOGLE_API_KEY environment variable not set. Using a placeholder key. Please set the environment variable for actual use.")
        # Use a hardcoded placeholder API key for demonstration if the environment variable is not set.
        api_key = "AIzaSyDYyffXJ0yk818WAp1RHb5sGPALbxv0x94"

    # Prompt the user for input.
    user_prompt = input("Enter your prompt: ")

    # Call the AI agent function with the determined API key and user prompt.
    response = run_ai_agent(api_key, user_prompt)

    # Print the AI's response.
    print(response)
