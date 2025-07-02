import streamlit as st
from tools.merge import merge_pdfs
import os

# Streamlit UI setup
st.set_page_config(page_title="PDF Toolbox", layout="centered")

st.title("📎 PDF Merger Tool")
st.markdown("Upload multiple PDFs to merge them into a single file.")

# Upload multiple files
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

# Merge button
if uploaded_files and st.button("🔗 Merge PDFs"):
    with st.spinner("Merging PDFs..."):
        merged_path = merge_pdfs(uploaded_files)

    st.success("✅ Merging complete!")
    with open(merged_path, "rb") as f:
        st.download_button("📥 Download Merged PDF", f, file_name="merged_output.pdf")

    os.remove(merged_path)
