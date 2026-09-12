import streamlit as st
import uuid
from database.database import get_connection

st.set_page_config(page_title="Evidence Grounded AI", page_icon="🤖", layout="wide")
st.title("🤖 Evidence-Grounded AI Assistant")
st.caption("Ask questions strictly based on uploaded research papers with source evidence citations.")

st.markdown("---")

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT id, name, text FROM documents")
docs = cursor.fetchall()

if not docs:
    st.warning("No documents found in library. Please upload a PDF in the Research Library first.")
else:
    doc_map = {d['name']: d['text'] for d in docs}
    selected_doc_name = st.selectbox("Select Document Context:", list(doc_map.keys()))
    doc_text = doc_map[selected_doc_name]
    
    query = st.text_input("Enter your research question:")
    
    if st.button("Search & Answer", type="primary"):
        if query:
            paragraphs = [p for p in doc_text.split('\n') if len(p.strip()) > 30]
            matched_evidence = [p for p in paragraphs if any(w.lower() in p.lower() for w in query.split())]
            
            evidence_str = "\n---\n".join(matched_evidence[:2]) if matched_evidence else "No direct lexical match found. Standard document context applied."
            answer_str = f"Based on '{selected_doc_name}', the document addresses this topic in the context of: {evidence_str[:300]}..."
            
            st.markdown("### 💡 Grounded Answer")
            st.info(answer_str)
            
            st.markdown("### 🔍 Source Evidence Citation")
            st.code(evidence_str if evidence_str else "Full document context referenced.")
            
            mem_id = str(uuid.uuid4())[:8]
            cursor.execute(
                "INSERT INTO ai_memories (id, question, answer, source_document, source_evidence) VALUES (?, ?, ?, ?, ?)",
                (mem_id, query, answer_str, selected_doc_name, evidence_str)
            )
            conn.commit()
            st.success("Answer & Evidence saved to Research Memory!")

conn.close()
