from PyPDF2 import PdfReader
import re
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter


class PdfTextProcesser:

    """Handles extraction and cleaning of text from PDF files."""

    @staticmethod
    @st.cache_data
    def extract_pdf_text(pdf_doc):
        text=""
        for pdf in pdf_doc:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text+=page.extract_text() or ''

        return text
    
    @staticmethod
    @st.cache_data
    def clean_text(raw_text):

        """Cleans the extracted text by removing duplicate spaces, punctuation,
       newlines, and fixing common OCR errors."""

        raw_text = re.sub(r'\s+', ' ', raw_text)  # Remove multiple spaces and newlines
        raw_text = re.sub(r'[^\w\s]', '', raw_text)  # Remove punctuation
        raw_text = re.sub(r'\bO\b', '0', raw_text)  # Fix common OCR errors
        raw_text = re.sub(r'\bPage \d+\b', '', raw_text)  # Remove page numbers
        raw_text = re.sub(r'(?:^|\s)([A-Za-z]+)(?:\s\1)+', r'\1', raw_text)  # Remove repeated words
        
        return raw_text.strip()
    
    @staticmethod
    @st.cache_data
    def chunk_text(clean_text,chunk_size=10000,chunk_overlap=1000):

        """handle the chunkcing of text data"""

        splitter=RecursiveCharacterTextSplitter()
        chunks=splitter.split_text(clean_text)

        return chunks
