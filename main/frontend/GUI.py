import streamlit as st
import pandas as pd

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from advisor_class import advisorBot
from ta_class import taBot
from api.chat_completion_api import ChatCompletionAPI
from frontend.ui_components import UIComponentFactory


class GUI:
    def __init__(self,chat_api:ChatCompletionAPI):
        
        self.advisor = advisorBot(chat_api)
        self.ta = taBot(chat_api)
        if 'advisor_conversation' not in st.session_state:
            st.session_state.advisor_conversation = []
        if 'ta_conversation' not in st.session_state:
            st.session_state.ta_conversation = []
        if 'selected_mode' not in st.session_state:
            st.session_state.selected_mode = None
        if 'visual_mode' not in st.session_state:
            st.session_state.visual_mode = "Light"


    def process_query(self,user_input, mode):
        if user_input:
            if mode == "UVU Advisor":
                conversation_key = 'advisor_conversation'
            else:
                conversation_key = 'ta_conversation'
            
            # conversation_key = 'advisor_conversation' if mode == "UVU Advisor" else 'ta_conversation'
            st.session_state[conversation_key].append(f"You: {user_input}")

            if mode == "UVU Advisor":
                response = self.advisor.query(user_input)
            else:  
                response = self.ta.query(user_input)

            st.session_state[conversation_key].append(f"{mode}: {response}")
    
    def run(self):
        #add columns
        setting,profile = st.columns(2)
        with setting:
            UIComponentFactory.styled_button_columns("settings")
        with profile:
            UIComponentFactory.styled_button_columns("profile")
        

        UIComponentFactory.create_backgroud()
        UIComponentFactory.create_title("UVU Advisor Bot")
        UIComponentFactory.create_sidebar_header("Welcome")

        st.sidebar.write("Choose color mode below")

        mode_color = UIComponentFactory.styled_colorbox("Select your mode:", ["Light", "Dark", "Custom"],help_text="Choose color preference")




        st.sidebar.write("Please select the mode and enter the query below")


        #modes for light and dark
        mode = UIComponentFactory.styled_selectbox("Select your mode:", ["UVU Advisor", "UVU TA"], help_text="Choose whether you want advice or tutoring.")
        if mode != st.session_state.selected_mode:
            st.session_state.selected_mode = mode
            if mode == "UVU Advisor":
                st.session_state.advisor_conversation = []
            else:  # mode == "UVU TA"
                st.session_state.ta_conversation = []
                

        user_input = UIComponentFactory.styled_text_input("Enter your query here:", "query", help_text="Type your question or request for the selected mode.")

        if mode == "UVU Advisor":
            conversation_key = 'advisor_conversation'
        else:
            conversation_key = 'ta_conversation'
        # conversation_key = 'advisor_conversation' if mode == "UVU Advisor" else 'ta_conversation'
        for message in st.session_state[conversation_key]:
            st.container().markdown(f"> {message}")

        if UIComponentFactory.styled_button("Submit", help_text="Click to submit your query."):
            self.process_query(user_input, mode)

    

if __name__ == "__main__":
    chat = ChatCompletionAPI(base_url='https://0e80-161-28-242-150.ngrok-free.app/v1')
    app = GUI(chat)
    app.run()
