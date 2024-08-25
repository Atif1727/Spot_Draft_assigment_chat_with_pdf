from langchain.chains.question_answering import load_qa_chain
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate


class QAChainBuilder:
    """Builds the question-answering chain."""

    def __init__(self,model="llama3"):
        self.model = model

    def build_chain(self):
        prompt_template = """
        Answer the question in as detailed manner as possible from the provided context. 
        If the answer is not in the provided context, just say, 
        "Answer is not available in the context." Do not provide a wrong answer.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        ollama_model=ChatOllama(model=self.model,temperature=0.5)#here we are using the ollama chat model
        prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
        chain=load_qa_chain(ollama_model,chain_type="stuff",prompt=prompt)

        return chain
