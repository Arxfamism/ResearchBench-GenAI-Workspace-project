import streamlit as st
import uuid
import pypdf
from database.database import get_connection

st.set_page_config(page_title="Research Library", page_icon="📚", layout="wide")
st.title("📚 Research Library Workspace")
st.caption("Upload research papers and laboratory protocols, preview contents, and view extracted text.")

st.markdown("---")

col_up, col_list = st.columns([1, 1])

with col_up:
    st.subheader("📤 Upload Document")
    uploaded_file = st.file_uploader("Select PDF File", type=["pdf"])
    doc_type = st.selectbox("Document Classification", ["Research Paper", "Laboratory Protocol"])
    
    if uploaded_file is not None:
        if st.button("Process & Save to Library", use_container_width=True):
            try:
                pdf_reader = pypdf.PdfReader(uploaded_file)
                extracted_text = ""
                for page in pdf_reader.pages:
                    extracted_text += page.extract_text() or ""
                
                doc_id = str(uuid.uuid4())[:8]
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO documents (id, name, type, text) VALUES (?, ?, ?, ?)",
                    (doc_id, uploaded_file.name, doc_type, extracted_text)
                )
                conn.commit()
                conn.close()
                st.success(f"Successfully processed and saved '{uploaded_file.name}'!")
            except Exception as e:
                st.error(f"Failed to process PDF: {e}")

with col_list:
    st.subheader("📁 Saved Documents & Reader")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type, upload_date, text FROM documents ORDER BY upload_date DESC")
    docs = cursor.fetchall()
    conn.close()

    if docs:
        doc_names = [f"{d['name']} ({d['type']})" for d in docs]
        selected_doc_idx = st.selectbox("Select document to view/open:", range(len(doc_names)), format_func=lambda x: doc_names[x])
        
        selected_doc = docs[selected_doc_idx]
        
        with st.container(border=True):
            st.markdown(f"#### 📄 {selected_doc['name']}")
            st.caption(f"ID: {selected_doc['id']} | Type: {selected_doc['type']} | Uploaded: {selected_doc['upload_date']}")
            
            with st.expander("📖 Open & Read Extracted Content", expanded=True):
                if selected_doc['text'].strip():
                    st.text_area("Document Text Content", selected_doc['text'], height=300)
                else:
                    st.warning("No extractable text found in this document.")
    else:
        st.info("No documents uploaded yet. Upload your first PDF on the left.")
