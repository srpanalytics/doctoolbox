import tempfile
import os
from pdf2docx import Converter
from pdf2image import convert_from_path
from PIL import Image
from datetime import datetime
import shutil

def convert_pdf(uploaded_file, convert_to):
    # Save uploaded file to disk first
    input_tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    uploaded_file.seek(0)
    input_tmp.write(uploaded_file.read())
    input_tmp.close()
    input_path = input_tmp.name

    # Unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    ext = convert_to.split('.')[-1]
    output_path = os.path.join(tempfile.gettempdir(), f"converted_{timestamp}.{ext}")

    if convert_to == "Word (.docx)":
        converter = Converter(input_path)
        converter.convert(output_path)
        converter.close()

    elif convert_to == "Image (.jpg)":
        images = convert_from_path(input_path)
        if images:
            images[0].save(output_path, 'JPEG')

    elif convert_to == "PDF/A":
        # Placeholder — just return original file
        shutil.copy(input_path, output_path)

    else:
        # Other conversions — basic copy for now
        shutil.copy(input_path, output_path)

    return output_path
