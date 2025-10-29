import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="PharmaDoc QA Assistant 💊", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.75rem;
        border-radius: 5px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("💊 PharmaDoc QA Assistant")
st.write("Ask domain-specific questions from pharmaceutical research papers")

# API endpoint
API_URL = "http://127.0.0.1:8000"

# Input section
st.header("📝 Enter Your Question")
query = st.text_input(
    "What would you like to know?", 
    placeholder="e.g., What are the side effects of Ibuprofen?",
    key="user_query"
)

# Ask button
if st.button("🔍 Ask", type="primary"):
    if query:
        with st.spinner("Searching through pharmaceutical documents..."):
            try:
                response = requests.post(f"{API_URL}/ask", json={"question": query})
                if response.status_code == 200:
                    result = response.json()
                    if result.get("status") == "success":
                        st.success("✅ Answer Found!")
                        st.info(result.get("answer"))
                    else:
                        st.error(f"Error: {result.get('error', 'Unknown error occurred')}")
                else:
                    st.error(f"API Error: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the backend API. Please make sure uvicorn is running at http://127.0.0.1:8000")
    else:
        st.warning("⚠️ Please enter a question first.")

# Information section
with st.expander("ℹ️ How to use this assistant"):
    st.write("""
    1. Enter your question about pharmaceutical research
    2. Click the 'Ask' button
    3. Get AI-powered answers from medical documents
    
    **Example questions:**
    - What are the side effects of Ibuprofen?
    - Summarize FDA safety recommendations for paracetamol
    - What are drug interactions with aspirin?
    """)

# Sidebar with configuration
st.sidebar.title("⚙️ Configuration")
st.sidebar.info("Backend API running at http://127.0.0.1:8000")
