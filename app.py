import streamlit as st
import os
from tools.merge import merge_pdfs
from tools.split import split_pdf
from tools.rotate import rotate_pdf
from tools.protect_unlock import encrypt_pdf, decrypt_pdf
from tools.watermark import add_watermark
from tools.convert import convert_pdf

st.set_page_config(page_title="PDF Toolbox", layout="wide")

st.title("All in one Doctoolbox")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📎 Merge", "✂️ Split", "🔁 Rotate",
    "🔐 Protect/Unlock", "🌊 Watermark", "🔄 Convert"
])

# ---- Tab 1: Merge PDFs ----
with tab1:
    st.subheader("📎 Merge PDFs")
    uploaded_files = st.file_uploader("Upload PDFs to merge", type=["pdf"], accept_multiple_files=True, key="merge")
    if uploaded_files and st.button("🔗 Merge PDFs"):
        with st.spinner("Merging PDFs..."):
            merged_path = merge_pdfs(uploaded_files)
        st.success("✅ Merging complete!")
        with open(merged_path, "rb") as f:
            st.download_button("📥 Download Merged PDF", f, file_name="merged_output.pdf")
        os.remove(merged_path)

# ---- Tab 2: Split PDFs ----
with tab2:
    st.subheader("✂️ Split PDF")
    split_file = st.file_uploader("Upload a PDF to split", type=["pdf"], key="split_upload")
    pages_input = st.text_input("Enter page numbers to extract (e.g., 1,3,5):", key="split_pages")
    if split_file and pages_input:
        page_numbers = [int(p.strip()) for p in pages_input.split(",") if p.strip().isdigit()]
        if st.button("✂️ Split PDF"):
            with st.spinner("Splitting PDF..."):
                split_results = split_pdf(split_file, page_numbers)
            st.success("✅ Splitting complete!")
            for result in split_results:
                with open(result["file_path"], "rb") as f:
                    st.download_button(
                        f"📥 Download Page {result['page']}", f,
                        file_name=f"page_{result['page']}.pdf"
                    )

# ---- Tab 3: Rotate PDFs ----
with tab3:
    st.subheader("🔁 Rotate PDF")
    rotate_file = st.file_uploader("Upload PDF to rotate", type=["pdf"], key="rotate_upload")
    direction = st.selectbox("Rotation direction", ["Clockwise (90°)", "Counterclockwise (-90°)"])
    if rotate_file and st.button("🔁 Rotate PDF"):
        with st.spinner("Rotating PDF..."):
            rotated = rotate_pdf(rotate_file, direction)
        st.success("✅ Rotation complete!")
        with open(rotated, "rb") as f:
            st.download_button("📥 Download Rotated PDF", f, file_name="rotated.pdf")
        os.remove(rotated)

# ---- Tab 4: Protect / Unlock ----
with tab4:
    st.subheader("🔐 Protect / Unlock PDF")
    action = st.radio("Select Action", ["Protect", "Unlock"])
    protect_file = st.file_uploader("Upload PDF", type=["pdf"], key="protect_upload")
    password = st.text_input("Enter Password", type="password")
    if protect_file and password and st.button("🔐 Process PDF"):
        with st.spinner("Processing..."):
            if action == "Protect":
                protected = encrypt_pdf(protect_file, password)
                label = "Encrypted"
            else:
                protected = decrypt_pdf(protect_file, password)
                label = "Decrypted"
        st.success(f"✅ {label} successfully!")
        with open(protected, "rb") as f:
            st.download_button(f"📥 Download {label} PDF", f, file_name=f"{label.lower()}_output.pdf")
        os.remove(protected)

# ---- Tab 5: Watermark ----
with tab5:
    st.subheader("🌊 Add Watermark")
    wm_file = st.file_uploader("Upload PDF to watermark", type=["pdf"], key="wm_upload")
    wm_text = st.text_input("Enter watermark text")
    if wm_file and wm_text and st.button("💧 Add Watermark"):
        with st.spinner("Watermarking PDF..."):
            watermarked = add_watermark(wm_file, wm_text)
        st.success("✅ Watermark added!")
        with open(watermarked, "rb") as f:
            st.download_button("📥 Download Watermarked PDF", f, file_name="watermarked.pdf")
        os.remove(watermarked)

# ---- Tab 6: Convert ----
with tab6:
    st.subheader("🔄 Convert PDF")
    convert_file = st.file_uploader("Upload PDF", type=["pdf"], key="convert_upload")
    convert_to = st.selectbox("Convert To", ["Word (.docx)", "Excel (.xlsx)", "PowerPoint (.pptx)", "Image (.jpg)", "HTML (.html)", "PDF/A"])
    if convert_file and st.button("🔁 Convert"):
        with st.spinner("Converting..."):
            output_file = convert_pdf(convert_file, convert_to)
        st.success("✅ Conversion complete!")
        with open(output_file, "rb") as f:
            st.download_button(f"📥 Download {convert_to}", f, file_name=f"converted.{convert_to.split('.')[-1]}")
        os.remove(output_file)
