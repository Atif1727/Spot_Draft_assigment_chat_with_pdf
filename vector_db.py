import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings

class VectorStoreManager:

    """Manages the creation and retrieval of the vector store."""

    def __init__(self,model="llama3"):
        self.model=model
    
    def create_vector_store(self,text_chunks):
        """Here we create a vector store and load the embeddings into it locally."""
        embeddings=OllamaEmbeddings(model=self.model)
        vector_store=FAISS.from_texts(text_chunks,embedding=embeddings)
        vector_store.save_local("faiss_index")

    def load_vector_store(self):
        """Here we load the embeddings from tyhe locally"""
        embeddings = OllamaEmbeddings(model=self.model)
        return FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)
