# 🚀 Quick Start Guide

> **Important:** Make sure you're in the project root directory (where `requirements.txt` is located) when running all commands.

## Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 2: Configure API Key
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get your API key from: https://makersuite.google.com/app/apikey

## Step 3: Build the Vector Database
```bash
python rag/rag_pipeline.py
```

This will:
- Load documents from `data/sample_papers/`
- Create embeddings
- Save to `faiss_index/` folder

## Step 4: Start the Backend
```bash
uvicorn app.backend:app --reload
```

Backend runs at: http://127.0.0.1:8000

## Step 5: Start the Frontend (New Terminal)
```bash
streamlit run app/frontend.py
```

Frontend opens at: http://localhost:8501

## ✅ You're ready!
Ask questions like:
- "What are the side effects of Ibuprofen?"
- "Summarize FDA safety recommendations for paracetamol"

---

## 🔧 Troubleshooting

### Issue: "Module not found"
**Solution:** Make sure you ran `pip install -r requirements.txt`

### Issue: "Google API key not found"
**Solution:** Create `.env` file with your Gemini API key (GOOGLE_API_KEY)

### Issue: "Vector database not found"
**Solution:** Run `python rag/rag_pipeline.py` to build the index

### Issue: "Backend connection error"
**Solution:** Make sure backend is running on port 8000
