# NVIDIA_NIM_Demo



# NVIDIA AI Document Q&A with LangChain and Streamlit

This project demonstrates how to use **NVIDIA’s AI Inference Endpoints** with **LangChain** and **Streamlit** to build an intelligent document-based Q&A system. It combines PDF ingestion, text chunking, FAISS vector search, and large language model reasoning to deliver context-aware answers directly from uploaded or directory-based documents.

<img width="1920" height="1149" alt="Screenshot 2025-10-30 012552" src="https://github.com/user-attachments/assets/3b0f8873-a1bb-45bf-b938-551c36b21ab5" />
<img width="1920" height="1152" alt="Screenshot 2025-10-30 013015" src="https://github.com/user-attachments/assets/2550bf8d-98f9-48ec-ac29-af858f8a57cb" />
<img width="1920" height="1143" alt="Screenshot 2025-10-30 013157" src="https://github.com/user-attachments/assets/a0934291-c2bb-4f3b-8a3d-4705022b8547" />






## Features

* ⚡ **NVIDIA Llama 3.3–70B Instruct Model** for natural language understanding and response generation
* 📄 **PDF ingestion** using `PyPDFDirectoryLoader`
* 🧩 **Text chunking** with `RecursiveCharacterTextSplitter` for efficient retrieval
* 🔍 **FAISS vector store** for semantic search and fast similarity matching
* 💬 **Conversational Q&A** powered by LangChain’s `create_retrieval_chain`
* 🌐 **Interactive Streamlit UI** for smooth user experience
* 🔑 **Environment-based NVIDIA API key loading** via `.env` file

---

## 🗂️ Project Structure

```
📁 NVIDIA-QA-App
│
├── app.py                 # Basic test script for NVIDIA API integration
├── finalapp.py            # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment file (contains your NVIDIA_API_KEY)
└── us_census/             # Folder containing sample PDF documents
```

---

## 🧰 Tech Stack

| Component               | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| **Streamlit**           | Web UI for user interaction              |
| **LangChain**           | Document loading, chunking, and chaining |
| **NVIDIA AI Endpoints** | Model inference and embeddings           |
| **FAISS**               | Vector-based semantic search             |
| **Python-dotenv**       | Securely load environment variables      |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/NVIDIA-QA-App.git
cd NVIDIA-QA-App
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root and add your **NVIDIA API key**:

```bash
NVIDIA_API_KEY=your_nvidia_api_key_here
```

---

## ▶️ Usage

### **Option 1: Run the Streamlit App**

```bash
streamlit run finalapp.py
```

**Steps:**

1. Place your PDF documents in the `us_census/` directory.
2. Click **“Document Embedding”** to build the FAISS vector store.
3. Type a question related to the documents in the input field.
4. View the generated answer and source document excerpts.

---

### **Option 2: Test NVIDIA API Connection**

Run the sample file:

```bash
python app.py
```

This verifies your NVIDIA model integration by generating a short article on Machine Learning.

---

## 🧩 Example Workflow

1. PDF documents are loaded using `PyPDFDirectoryLoader`.
2. Text is split into manageable chunks with overlaps.
3. Each chunk is converted into embeddings using **NVIDIAEmbeddings**.
4. FAISS builds a searchable index of document vectors.
5. When a query is entered, LangChain retrieves the most relevant text chunks.
6. The **Llama 3.3–70B model** provides a contextually accurate answer.

---

## 📘 Requirements

Make sure your `requirements.txt` file includes:

```
openai
python-dotenv
langchain_nvdia_ai_endpoints
langchain_community
faiss-cpu
streamlit
pypdf
```

---

## 🧠 Example Questions

Try asking:

* “What are the key points mentioned in the document?”
* “Summarize the data insights from the census file.”
* “Explain the main findings from the uploaded PDFs.”

---

## 💡 Future Improvements

* Add **file uploader** for dynamic PDF uploads
* Integrate **chat history** using Streamlit session state
* Extend to **multi-document querying**
* Deploy on **Render** or **Streamlit Cloud**

---

## 👩‍💻 Author

**Divya Khanolkar**
💼 Passionate about AI and intelligent automation
🌐 [LinkedIn Profile (optional)](https://www.linkedin.com/in/divyakhanolkar)

