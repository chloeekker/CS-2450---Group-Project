import streamlit as st

# Header
st.title("UVUAdvisor Bot")


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("What-If"):
        # Handle What-If button click
        pass
with col2:
    if st.button("Search"):
        # Handle Search button click
        pass
with col3:
    if st.button("My Profile"):
        # Handle My Profile button click
        pass

# Chat Area
st.subheader("Chat with UVUAdvisor Bot")

chat_history = [
    {"sender": "UVUAdvisor Bot", "message": "Hello! How can I assist you today?"},
    {"sender": "User", "message": "I'd like to know about course requirements for Computer Science."},

]

for chat in chat_history:
    if chat["sender"] == "UVUAdvisor Bot":
        st.text_area("UVUAdvisor Bot:", chat["message"], disabled=True)
    else:
        st.text_area("User:", chat["message"], disabled=True)

# Input Bar
user_input = st.text_input("Type your message here:", "")


if st.button("Send"):
    # Handle sending message
    pass
