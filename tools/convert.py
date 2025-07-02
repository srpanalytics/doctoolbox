import tempfile
from pdf2docx import Converter
from pdf2image import convert_from_path
from PIL import Image

def convert_pdf(uploaded_file, convert_to):
    # 1. Save uploaded file to a temporary path
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        uploaded_file.seek(0)  # 🛠 Reset pointer to beginning
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    output_ext = convert_to.split('.')[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_ext}") as out_tmp:
        output_path = out_tmp.name

    if convert_to == "Word (.docx)":
        converter = Converter(tmp_path)
        converter.convert(output_path)
        converter.close()

    elif convert_to == "Image (.jpg)":
        images = convert_from_path(tmp_path)
        if images:
            images[0].save(output_path, 'JPEG')

    elif convert_to == "PDF/A":
        # Just return original file as a placeholder
        return tmp_path

    return output_path
