import tempfile
import os
from pdf2docx import Converter
from pdf2image import convert_from_path

def convert_pdf(pdf_file, convert_to):
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=f".{convert_to.split('.')[-1]}").name

    if convert_to == "Word (.docx)":
        converter = Converter(pdf_file)
        converter.convert(output_path)
        converter.close()

    elif convert_to == "Image (.jpg)":
        images = convert_from_path(pdf_file)
        if images:
            images[0].save(output_path, 'JPEG')

    else:
        with open(output_path, "wb") as out:
            out.write(pdf_file.read())

    return output_path
