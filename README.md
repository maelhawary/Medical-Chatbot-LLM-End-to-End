# Medical-Chatbot-LLM-End-to-End

# Question-Answer-Web-App

This is an LLM demo project for answering questions related to medical issues. By running the web-app, you can ask any questions (e.g. What is Truma or What is the treamtment of X, or I have some symptoms Y what this could be, etc...) and you will get an accurate and presice reply. The LLM model is based on google-flan-t5-base which you need to download before using the model(https://huggingface.co/google/flan-t5-base). The implementation of this project includes the following packages: Langchain and Huggingface for data preprocessing, embeddings and vector-database, as well as Streamlit for web-app interface. 

# To use
Install requirements using,

```bash
pip install -r requirements.txt
```
Then, run the app as follows:
```bash
streamlit run web-app.py
```
