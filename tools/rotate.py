from PyPDF2 import PdfReader, PdfWriter
import tempfile

def rotate_pdf(pdf_file, direction="Clockwise (90°)"):
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        if direction == "Clockwise (90°)":
            page.rotate(90)
        else:
            page.rotate(-90)
        writer.add_page(page)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    with open(temp_file.name, "wb") as f:
        writer.write(f)

    return temp_file.name
