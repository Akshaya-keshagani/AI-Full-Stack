import ollama
import streamlit as st
st.title("HI I AM SIRI")
with st.sidebar:
    personalities={"Kid😊":"give the answers like you are expalining to  5 year old kid.Give the answer in 2 lines",
                   "Professor🧑‍🏫":"you are an 'IIT professor'. Explain the topics using correct terminology.Give in 2 lines",
                   "Doctor😷":"Assume you are a doctor. Explain the terminology which are mostly used in medical field. Give answer in two lines"}
    personality=st.selectbox("select a personality",personalities.keys())
    st.title("CHAT SETTINGS")
    if st.button("clear cache"):
        st.session_state.messages=[]
        st.success("succesfully cleared the chat")
    uploaded_file=st.file_uploader("upload a file...")
    if uploaded_file is not None:
        st.success("file uploaded successfully")
        st.balloons()
        st.snow()
        
        with st.expander("preview"):
            context=uploaded_file.read().decode("utf-8")
            st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question=st.chat_input("you:")

        

if question:
    with st.chat_message("user"):
        st.write("user:",question)


    st.session_state.messages.append({"role":"user",
                 "content":question})
    
    with st.spinner("Thinking..."):
        response=ollama.chat(
            model="llama3.2:3b",
            messages=[{"role":"system","content":personalities[personality]}]+st.session_state.messages
        )
    with st.chat_message("assistant"):

        st.write("AI:",response["message"]["content"])
    st.session_state.messages.append({"role":"assistant",
                 "content":response["message"]["content"]})