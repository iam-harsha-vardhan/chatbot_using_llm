import streamlit as st
from langchain_community.llms import Ollama

# Error handling (assuming Ollama might raise exceptions during initialization)
try:
  llm = Ollama(model="llama3")
except Exception as e:
  st.error(f"Error initializing Ollama: {e}")
  raise  # Re-raise to stop Streamlit app from continuing

st.title("Chatbot using Llama3")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
  if prompt:
    with st.spinner("Generating response..."):
      try:
        st.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))
      except Exception as e:
        st.error(f"Error generating response: {e}")
