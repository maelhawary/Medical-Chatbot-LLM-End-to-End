import streamlit as st
import LLM_pipline as llm
import tempfile


st.set_page_config(layout='wide',page_title='Medical Chatbot Web-APP')
def main(embd_name,llm_name,VB_path):
    st.title('Medical Chatbot Web-App')

    question = st.text_input("How I can help you?, Please enter your question or inquiry")
    if st.button("Show Q and A"):
        #filepath =uploaded_file.name
        #with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
           # tmp_file.write(uploaded_file.read())
            #filepath = tmp_file.name
        answer = llm.llm_reply(question,VB_path,embd_name,llm_name)
        #answer = ans_chain.run(question)
        st.text("____Answer____")
        st.text(answer)


if __name__ == '__main__':
    embd_name="BAAI/bge-large-en"
    llm_name = "google\\flan-t5-base"
    VB_path= "store/med_vdb"

    main(embd_name,llm_name,VB_path)
