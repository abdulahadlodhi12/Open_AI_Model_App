import streamlit as st
import langchain_openai as OpenAI
st.title("Quick Start App")
open_ai_key = st.sidebar.text_input("OpenAI Api Key")
def generate_response(input_text):
    llm = OpenAI(temperature = 0.6,open_api_key=open_ai_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area("Enter Your Prompt")
    submitted = st.form_submit_button("Submit")
    if not open_ai_key.startswith('sk-'):
        st.warning("Please Enter Correct OpenAI Api Key")
    if submitted and open_ai_key.startswith('sk-'):
        generate_response(text)
    
