import json
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import JSONLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
# Loaded all the secret keys
load_dotenv()

# created openai instance to interact with the openai models
LLM = ChatOpenAI(model="gpt-4o-mini")

# created the an in memory vector store and stored all the product details there


def create_db(items):
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(items, embeddings)
    return vector_db
