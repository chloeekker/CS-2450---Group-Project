import streamlit as st



def chat_bubble(sender, message, color):
    '''
    Creates message bubbles for chat
    '''

    st.markdown(f'<div style="background-color: {color}; padding: 10px; border-radius: 10px; margin: 5px;">'
                f'<p style="margin: 0;">{sender}</p>'
                f'<p style="margin: 0;">{message}</p>'
                f'</div>', unsafe_allow_html=True)
    


def send(user, message, color):
    '''
    
    '''
    chat_bubble(user, message, color)



def main():
    # Header
    st.title("UVUAdvisor Bot")


    settingButton,whatIfButton, searchButton, myProfileButton = st.columns(4)
    with settingButton:
        if st.button("Setting"):
            #Handle settings button (such as color changes)
            pass
    with whatIfButton:
        if st.button("What-If"):
            # Handle What-If button click
            pass
    with searchButton:
        if st.button("Search"):
            # Handle Search button click
            pass
    with myProfileButton:
        if st.button("My Profile"):
            # Handle My Profile button click
            pass

    # Chat Area
    st.subheader("Chat with UVUAdvisor Bot")

    chat_history = [
        {"sender": "UVUAdvisor Bot", "message": "Hello! How can I assist you today?", "color": "green"},
        {"sender": "User", "message": "I'd like to know about course requirements for Computer Science.", "color": "grey"}
    ]
    for chat in chat_history:
        chat_bubble(chat["sender"], chat["message"], chat["color"])


    # Input Bar
    user_input = st.text_input("Type your message here:", "")


    if st.button("Send"):
        # Handle sending message
        chat_history.append({"sender": "User", "message": user_input, "color": "grey"})
        send("User", user_input, "grey")
        
        pass

if __name__ == "__main__":
    main()
