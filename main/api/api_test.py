"""
Chloe, Aaron, Eric
UVU Advisor Bot

api_test.py
"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from chat_completion_api import ChatCompletionAPI

def main():
    chat_api = ChatCompletionAPI()

    messages = "What are the prerequisites for CS 2450?"
    response = chat_api.post_completions(messages, stream=False)
    message = response["choices"][0]["message"]["content"]

    print(message)

if __name__=="__main__":
    main()