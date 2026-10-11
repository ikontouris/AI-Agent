import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from functions.call_function import available_functions

def generate_content(client,messages):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
         tools=available_functions)
    return response