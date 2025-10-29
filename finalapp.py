
import streamlit as st
import os
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import time

# Load the NVIDIA API key
load_dotenv()
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")

# Initialize the NVIDIA LLM
llm = ChatNVIDIA(model="meta/llama-3.3-70b-instruct")

# Function to create vector embeddings
def vector_embedding():
    # Initialize session state variables if not already set
    if "embeddings" not in st.session_state:
        st.session_state.embeddings = NVIDIAEmbeddings()

    if "loader" not in st.session_state:
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")

    if "documents" not in st.session_state:
        st.session_state.documents = st.session_state.loader.load()

    if "text_splitter" not in st.session_state:
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50)

    #  Fix: use 'documents' instead of undefined 'docs'
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(
        st.session_state.documents[:30]
    )

    # Create FAISS vector store
    st.session_state.vectors = FAISS.from_documents(
        st.session_state.final_documents, st.session_state.embeddings
    )

# Streamlit UI

st.title("NVIDIA Demo")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    Questions: {input}
    """
)

prompt1 = st.text_input("Enter your question from the documents")

# When button is clicked
if st.button("Document Embedding"):
    vector_embedding()
    st.success("FAISS Vector Store DB is ready using NVIDIA Embeddings")

# Handle user query
if prompt1:
    if "vectors" not in st.session_state:
        st.warning("Please create the document embeddings first.")
    else:
        retriever = st.session_state.vectors.as_retriever()

        # Build retrieval chain correctly
        document_chain = create_stuff_documents_chain(llm, prompt, output_parser=StrOutputParser())
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        start = time.process_time()
        response = retrieval_chain.invoke({"input": prompt1})
        st.write("Response Time:", round(time.process_time() - start, 2), "seconds")

        st.subheader("Answer:")
        st.write(response["answer"])

        # Show retrieved document sources
        with st.expander(" See Document Sources"):
            for i, doc in enumerate(response["context"]):
                st.write(f"**Document {i+1}:**")
                st.write(doc.page_content)
                st.write("-------------------------------------")



        

