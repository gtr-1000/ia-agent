
import streamlit as st
from openai import OpenAI

# 1. Configure the Streamlit page
st.set_page_config(page_title="ChatBot with AI", page_icon="🤖")
st.title("ChatBot with AI")

# 2. Load the API key from local Streamlit secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except (KeyError, FileNotFoundError):
    st.error(
        "API key not found. Configure GOOGLE_API_KEY "
        "in .streamlit/secrets.toml."
    )
    st.stop()

# 3. Initialize the Gemini client using the OpenAI-compatible API
modelo = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    max_retries=3,
)

# 4. Initialize the conversation history for this session
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# 5. Display the previous messages
for mensagem in st.session_state["lista_mensagens"]:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# 6. Get the user's input
mensagem_usuario = st.chat_input("Type your message here")

if mensagem_usuario:
    # Display and save the user's message
    with st.chat_message("user"):
        st.write(mensagem_usuario)

    st.session_state["lista_mensagens"].append(
        {"role": "user", "content": mensagem_usuario}
    )

    # Request a response from Gemini and handle API errors
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                resposta_modelo = modelo.chat.completions.create(
                    model="gemini-3.8-flash",
                    messages=st.session_state["lista_mensagens"],
                )

            resposta_ia = resposta_modelo.choices[0].message.content

            if not resposta_ia:
                resposta_ia = "The model returned an empty response."

            st.write(resposta_ia)

        # Save the assistant's response to the conversation history
        st.session_state["lista_mensagens"].append(
            {"role": "assistant", "content": resposta_ia}
        )


    except Exception as e:
        # Remove the failed user message so it can be retried
        st.session_state["lista_mensagens"].pop()

        # Display the actual error for debugging
        st.error(f"Error type: {type(e).__name__}")
        st.code(str(e))
 