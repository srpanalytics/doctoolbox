import tempfile
import os
from pdf2docx import Converter
from pdf2image import convert_from_path
from PIL import Image
from datetime import datetime
import shutil

def convert_pdf(uploaded_file, convert_to_label):
    # Map label to extension
    convert_map = {
        "Word (.docx)": "docx",
        "Excel (.xlsx)": "xlsx",
        "PowerPoint (.pptx)": "pptx",
        "Image (.jpg)": "jpg",
        "HTML (.html)": "html",
        "PDF/A (.pdf)": "pdf"
    }

    ext = convert_map.get(convert_to_label, "pdf")

    # Save uploaded PDF to temp path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        uploaded_file.seek(0)
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    output_path = os.path.join(tempfile.gettempdir(), f"converted_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}")

    if ext == "docx":
        converter = Converter(tmp_path)
        converter.convert(output_path)
        converter.close()

    elif ext == "jpg":
        images = convert_from_path(tmp_path)
        if images:
            images[0].save(output_path, 'JPEG')

    elif ext == "pdf":
        # Just copy original for now
        shutil.copy(tmp_path, output_path)

    else:
        # Excel/PPT/HTML → not supported locally, placeholder
        shutil.copy(tmp_path, output_path)

    return output_path
