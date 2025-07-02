from PyPDF2 import PdfMerger
import os
import tempfile

def merge_pdfs(uploaded_files):
    merger = PdfMerger()

    for pdf in uploaded_files:
        merger.append(pdf)

    merged_pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    with open(merged_pdf_path, "wb") as fout:
        merger.write(fout)

    merger.close()
    return merged_pdf_path
