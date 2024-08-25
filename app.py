import streamlit as st
from Ingestion import PdfTextProcesser
from vector_db import VectorStoreManager
from Reteriver import QAChainBuilder


class PdfChatApp:

    """Main class for the Streamlit app."""

    def __init__(self,model):
        # Initialize session state if not already present
        if "message" not in st.session_state:
            st.session_state.messages=[]

        self.vector_store_manager = VectorStoreManager(model=model)
        self.pdf_text_processor = PdfTextProcesser()
        self.qa_chain_builder = QAChainBuilder(model=model)
 
    def process_pdfs(self,pdf_docs):

        """Process and index the uploaded PDF documents."""

        raw_text=self.pdf_text_processor.extract_pdf_text(pdf_doc=pdf_docs)
        clean_text=self.pdf_text_processor.clean_text(raw_text)
        text_chunks=self.pdf_text_processor.chunk_text(clean_text)
        self.vector_store_manager.create_vector_store(text_chunks)
        st.success("Done")

    def get_response(self,input_query):

        """Get a response to a user query based on the processed PDFs."""

        docs = self.vector_store_manager.load_vector_store().similarity_search(input_query)
        chain=self.qa_chain_builder.build_chain()
        response=chain.invoke({"input_documents": docs, "question": input_query}, return_only_outputs=True)

        return response
    
    def display_chat_messages(self):

        """Display all chat messages stored in session state."""

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


    def handle_user_input(self):

        """Handle user input from the chat interface."""

        if input_query := st.chat_input("Ask a Question from the PDF Files"):
            st.session_state.messages.append({"role": "user", "content": input_query})
            with st.chat_message("user"):
                st.markdown(input_query)
            response=self.get_response(input_query)# get the response from the model
            with st.chat_message("assistant"):
                st.markdown(response['output_text'])
            st.session_state.messages.append({"role":"assistant","content":response["output_text"]})


    def run(self):

        """Run the Streamlit app."""
        
        st.set_page_config(page_title="Chat PDF", page_icon=":file_pdf:")
        st.markdown("<h1 style='color: #3498db; text-align: center;'>Chat with PDFs</h1>", unsafe_allow_html=True)

        with st.sidebar:
            st.title("Menu:")
            pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)

            if st.button("Submit & Process"):
                with st.spinner("Processing..."):
                    self.process_pdfs(pdf_docs)

        self.display_chat_messages()
        self.handle_user_input()


if __name__ == "__main__":
    app=PdfChatApp(model="llama3")
    app.run()
