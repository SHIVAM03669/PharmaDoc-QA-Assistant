# 💊 PharmaDoc QA Assistant

An AI-powered assistant that allows users to query pharmaceutical research documents using Retrieval-Augmented Generation (RAG) and LLMs.

## 🎯 Objective
Help pharma researchers, QA specialists, and data scientists quickly find insights from drug-related documents using natural language queries.

---

## ⚙️ Tech Stack
- **Language:** Python  
- **LLM:** Google Gemini Pro  
- **Retrieval:** FAISS  
- **Frameworks:** LangChain, FastAPI, Streamlit  

---

## 🧠 How It Works
1. Load and split pharma research PDFs into text chunks  
2. Create embeddings and store them in a FAISS vector database  
3. Query user input → retrieve relevant chunks → generate contextual answer using LLM  
4. Display answer in a Streamlit web app  

---

## 🚀 Run Locally

### Prerequisites
- Python 3.8+
- Google Gemini API key (get it from https://makersuite.google.com/app/apikey)

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/PharmaDoc-QA-Assistant.git
cd PharmaDoc-QA-Assistant
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Add Sample Documents
Place pharmaceutical PDF documents in the `data/sample_papers/` folder.

### 5. Build Vectorstore
```bash
python rag/rag_pipeline.py
```

### 6. Run Backend
```bash
uvicorn app.backend:app --reload
```
The backend will run at `http://127.0.0.1:8000`

### 7. Run Frontend (in a new terminal)
```bash
streamlit run app/frontend.py
```
The frontend will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure
```
PharmaDoc-QA-Assistant/
├── data/
│   └── sample_papers/          # Place your .pdf documents here
├── etl/
│   └── load_and_clean.py       # Document loading and chunking
├── rag/
│   └── rag_pipeline.py         # Vector store and QA chain
├── app/
│   ├── backend.py              # FastAPI endpoints
│   └── frontend.py             # Streamlit UI
├── faiss_index/                # Auto-generated vector database
├── requirements.txt
└── README.md
```

---

## 🎯 Example Queries
- "What are the side effects of Ibuprofen?"
- "Summarize FDA safety recommendations for paracetamol"
- "What are drug interactions with aspirin?"

---

## 🔧 API Endpoints

### POST /ask
Query the pharmaceutical documents.

**Request:**
```json
{
  "question": "What are the side effects of Ibuprofen?"
}
```

**Response:**
```json
{
  "answer": "According to the research documents...",
  "status": "success"
}
```

---

## 📝 Notes
- Make sure to add your Google Gemini API key in the `.env` file
- The first run requires building the vectorstore (step 5)
- FAISS index is stored locally after the first run for faster subsequent queries

---

## 🤝 Contributing
Feel free to submit issues and enhancement requests!

---

## 📄 License
MIT License
