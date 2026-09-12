import os
import sys
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="ResearchBench AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize DB safely
try:
    from database.database import initialize_database
    initialize_database()
except Exception as e:
    st.sidebar.error(f"DB Init Error: {e}")

st.markdown("""
<style>
    .main-title { font-size: 2.6rem; font-weight: 800; color: #00C9FF; margin-bottom: 0px; }
    .sub-title { color: #94a3b8; font-size: 1.1rem; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🧬 ResearchBench AI")
st.sidebar.caption("HEC / Aspire GenAI Hackathon MVP")
st.sidebar.markdown("---")
st.sidebar.caption("👨‍💻 Developed by **Arsalan & Habiba**")

st.markdown('<p class="main-title">🧬 ResearchBench AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI-Powered Persistent Workspace for Biotechnology & Life Sciences</p>', unsafe_allow_html=True)

st.success("👈 **Navigation Active:** Left sidebar me kisi bhi module par click karke workspace explore karein!")

st.divider()

m1, m2, m3, m4 = st.columns(4)
m1.metric("📚 Research Papers", "Active RAG", delta="PDF Extraction")
m2.metric("🤖 AI Chat", "Grounded", delta="Evidence Linked")
m3.metric("🧠 Research Memory", "SQLite Store", delta="Persistent")
m4.metric("🛡️ Safety Engine", "Enabled", delta="SDS Alerts")

st.divider()

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("#### 📚 1. Research Library & PDF Reader")
        st.caption("Upload biotechnology papers, extract text, and view original PDF contents directly inside the app.")
    with st.container(border=True):
        st.markdown("#### 📋 2. Protocol Companion & Safety Alerts")
        st.caption("Convert lab PDF procedures into interactive checklists with automatic hazard reagent detection.")

with col2:
    with st.container(border=True):
        st.markdown("#### 🧠 3. Persistent Research Memory")
        st.caption("Preserve research questions, AI answers, personal hypotheses, and experimental observations.")
    with st.container(border=True):
        st.markdown("#### 🗺️ 4. Research Journey & Dashboard")
        st.caption("Visualize connected events from literature reading to lab protocol execution.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #64748b; font-size: 13px;'>ResearchBench AI — Preserving the researcher's journey through scientific literature.<br>Created by <b>Arsalan & Habiba</b></div>", unsafe_allow_html=True)

