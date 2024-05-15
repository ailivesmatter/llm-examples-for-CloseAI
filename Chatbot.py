from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("CloseAI API Key", key="chatbot_api_key", type="password")
    model_options = ["gpt-4-turbo","gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4-vision-preview"]
    selected_model = st.sidebar.selectbox("Select Model", model_options)    
    "[Get an CloseAI API key](https://referer.shadowai.xyz/r/1003298)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/sturdy-fishstick-ggr5jvxgr792vv?editor=web)"

st.title("💬 CloseAI DemoChat")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key,base_url="https://api.closeai-proxy.xyz/v1")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=selected_model, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
