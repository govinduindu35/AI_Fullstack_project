import ollama
import streamlit as st
st.title(":rainbow[Welcome to my ChatBot App!!!]👽")
with st.sidebar:
    st.header(":blue[Chat Settings⚙️]")
    if st.button("Clear Chat🗑️"):
        st.session_state.messages = []
        st.success("Chat cleared👍")
    personalities = {
        "kid👶" : "Answer the question like you are responding to a 5 year old kid. Give the answer in 2 lines only",
        "Friend🤝" : "Answer the question in a friendly and casual manner. Give me the answer in 2 lines only",
        "Scientist 🤖" : "Answer the question. Give me the answer in 2 lines only"
    }
    personality = st.selectbox("Select a personality", personalities.keys())
    uploaded_file = st.file_uploader("🤔upload a text file...")
    try:
        if uploaded_file:
          st.success("👍File uploaded successfully")
          context = uploaded_file.read().decode("utf-8")
          if st.button("Display👀"):
            st.text(context)
    except:
        st.error("Error👎")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question=st.chat_input("Ask question: ❓")
if question:
    st.session_state.messages.append(
    {
        "role": "user",
        "content": question
    }
    )
    with st.chat_message("user"):
         st.write(question)
         with st.spinner("Thinking...💭"):
             response = ollama.chat(
                  model="llama3.2.:3b",
                  messages= [
                    {"role" : "system", "content": personalities[personality]}]
                        + st.session_state.messages)
    st.session_state.messages.append(
        {"role": "assistant",
        "content": response["message"]["content"]}
    )
    with st.chat_message("assistant"):
     st.write("AI:", response["message"]["content"])