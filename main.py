import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from helper import generate_content
from prompts import system_prompt
import json
from functions.call_function import call_function
import sys

def main():
    
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None :
        raise RuntimeError("No key found")
    

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt}]
    
    for _ in range(20):
        response = generate_content(client,messages)
        

        if response.usage is None:
            raise RuntimeError("Failed API request")
        
        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}")
            print (f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
    

        message= response.choices[0].message
        messages.append(message)
        verbose = args.verbose
        if message.tool_calls :
            for tool_call in message.tool_calls:
                
                result_message = call_function(tool_call,verbose)
                if not result_message.get("content"):
                    raise RuntimeError("The function returned no content")
                if verbose :
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
                
        else :
            print(message.content)
            break
    else:
        print("No final solution out of loops")
        sys.exit(1)
        

if __name__ == "__main__":
    main()
