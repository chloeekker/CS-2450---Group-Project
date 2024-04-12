from typing import Optional

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from api.conversation import Conversation, Message
from api.chat_completion_api import ChatCompletionAPI
from api.role import Role

class advisorBot:
    def __init__(self, chat_api : ChatCompletionAPI):
        self.chat_api = chat_api
        self.context = "You are a UVU advisor; give advice and speak professionally."
    
    def query(self, query : str):
        response = self.chat_api.post_completions(query, stream=False, role=Role.USER)
        if response and 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['message']['content']
        else:
            return "I'm sorry, I couldn't find an answer to your question."