import tempfile
import os
from pdf2docx import Converter
from pdf2image import convert_from_path
from PIL import Image

def convert_pdf(uploaded_file, convert_to):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    output_ext = convert_to.split('.')[-1]
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_ext}").name

    if convert_to == "Word (.docx)":
        converter = Converter(tmp_path)
        converter.convert(output_path)
        converter.close()

    elif convert_to == "Image (.jpg)":
        images = convert_from_path(tmp_path)
        if images:
            images[0].save(output_path, 'JPEG')

    elif convert_to == "PDF/A":
        # Just return the original PDF for now
        return tmp_path

    else:
        with open(output_path, "wb") as out:
            out.write(uploaded_file.read())

    return output_path
