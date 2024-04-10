from typing import Optional

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from api.conversation import Conversation, Message
from chat_api import ChatCompletionAPI
from chat_api import Role



class taBot:
    def __init__(self, chat_api: ChatCompletionAPI):
        self.chat_api = chat_api

    def query(self,query:str):
        response = self.chat_api.post_chat_completions(query, role=Role.USER, is_init=False)
        if response and 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['message']['content']
        else:
            return "I'm sorry, I couldn't find an answer to your question."
                