import tempfile
import os
from pdf2docx import Converter
from pdf2image import convert_from_path
from PIL import Image
from datetime import datetime
import shutil

def convert_pdf(uploaded_file, convert_to_label):
    # Clean extension mapping
    convert_map = {
        "Word (.docx)": "docx",
        "Excel (.xlsx)": "xlsx",
        "PowerPoint (.pptx)": "pptx",
        "Image (.jpg)": "jpg",
        "HTML (.html)": "html",
        "PDF/A (.pdf)": "pdf"
    }
    ext = convert_map.get(convert_to_label, "pdf")

    # 1. Save uploaded PDF to disk
    input_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    # 2. Generate clean output filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = os.path.join(tempfile.gettempdir(), f"converted_{timestamp}.{ext}")

    # 3. Handle different formats
    if ext == "docx":
        converter = Converter(input_path)
        converter.convert(output_path)
        converter.close()

    elif ext == "jpg":
        images = convert_from_path(input_path)
        if images:
            images[0].save(output_path, "JPEG")

    elif ext == "pdf":
        shutil.copy(input_path, output_path)

    else:
        shutil.copy(input_path, output_path)

    return output_path
