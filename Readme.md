# Chat with PDF using the AI

Welcome to the "Chat PDF with ollama" Streamlit app! This application allows you to interact with PDF documents by asking questions and receiving detailed answers based on the content of the uploaded PDFs. The app uses Streamlit, LangChain, and ollama model to provide a seamless chat experience.

## Setup Instructions

### Prerequisites

1. **Python**: Ensure that you have Python 3.7 or higher installed. Download it from the [official Python website](https://www.python.org/downloads/).

2. **Pip**: Make sure you have pip installed to manage Python packages. Check this by running `pip --version` in your terminal.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Atif1727/Spot_Draft_assigment_chat_with_pdf.git
   cd chat_with_pdf
2. **Create a Virtual Environment (Optional but Recommended)**:
    ```bash
    python -m venv venv
    venv\Scripts\activate # On linux use `source venv/bin/activate`
3. **Install Dependencies**:
    #### Install the required Python packages using the requirements.txt file.
    ```bash
    pip install -r requirements.txt
4. **Obtain and Set Up for Ollama**:
    * **Download Ollama:**:Visit the [Ollama website](https://ollama.com/) and follow the instructions to download and install Ollama for your operating system.
    * **Pull Llama 3 Model**: Use the following command to download the Llama 3 model through Ollama in our system.
    ```bash
    ollama pull 'model_name'
5. * **Run ollama model**:Use the following command to run the model in local.
    ```bash
    ollama run 'model_name'

## Usage Guide

### Running the Streamlit App
1. **Start the Streamlit Server**:
    ```bash
    streamlit run app.py
2. **Open Your Web Browser**:

    The app will be available at http://localhost:8501 by default. Open this URL in your web browser to access the app.\

### using the App

1. **Upload PDF Files**:
    * Click on the "Upload your PDF Files and Click on the Submit & Process Button" section in the sidebar to upload your PDF documents.

2. **Process PDFs**:
    * After uploading the PDFs, click the "Submit & Process" button. The app will extract and preprocess text from the PDFs, chunk it, and store it in a vector database for querying.

3. **Ask Questions**:
    * Use the text input box to ask questions about the uploaded PDF files. The app will use the stored data to provide responses.

4. **View Responses**:
    * Responses to your questions will be displayed on the main page of the app.

#### Note on using Ollama Model
    Due to limited access to other APIs, such as Anyscale and OpenAI, we are utilizing the Ollama model for our application. Ollama provides a robust and effective alternative that meets our needs for natural language processing and interaction with PDF documents. By using Ollama, we ensure continued functionality and performance while navigating the limitations in access to other API services. This approach allows us to proceed with the development and deployment of our application without interruption.
    

### Troubleshooting

* **Missing Dependencies** : Ensure all required packages are installed as listed in requirements.txt.

* **API Key Issues**: Verify that the API key is correctly set up and accessible by the application.

* **File Upload Errors**: Check the format and size of the uploaded PDF files.


## download the sample pdf file from here

https://drive.google.com/file/d/1eTZkEPlaNrjmjCYGu03GLILypPFbhg7C/view?usp=sharing


### One page documentation to explain the challenges and potentsional improvements

https://docs.google.com/document/d/1fCrx1UHZt7zcQCp0NeMkf4e_5IOWbj92k-uk7y4q194/edit