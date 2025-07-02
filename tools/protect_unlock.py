from PyPDF2 import PdfReader, PdfWriter
import tempfile

def encrypt_pdf(pdf_file, password):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    with open(temp_file.name, "wb") as f:
        writer.write(f)

    return temp_file.name

def decrypt_pdf(pdf_file, password):
    reader = PdfReader(pdf_file)
    if reader.is_encrypted:
        try:
            reader.decrypt(password)
        except Exception as e:
            raise ValueError("Invalid password")
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    with open(temp_file.name, "wb") as f:
        writer.write(f)

    return temp_file.name
