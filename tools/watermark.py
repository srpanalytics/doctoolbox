from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import grey
import tempfile

def create_watermark(watermark_text):
    watermark_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(watermark_file.name, pagesize=letter)
    c.setFont("Helvetica-Bold", 40)
    c.setFillColor(grey, alpha=0.2)
    c.drawCentredString(300, 400, watermark_text)
    c.save()
    return watermark_file.name

def add_watermark(pdf_file, watermark_text):
    watermark_path = create_watermark(watermark_text)

    base = PdfReader(pdf_file)
    watermark = PdfReader(watermark_path)
    watermark_page = watermark.pages[0]

    writer = PdfWriter()
    for page in base.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    with open(temp_file.name, "wb") as f:
        writer.write(f)

    return temp_file.name
