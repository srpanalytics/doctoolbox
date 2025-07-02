from PyPDF2 import PdfReader, PdfWriter
import tempfile

def split_pdf(pdf_file, split_pages):
    reader = PdfReader(pdf_file)
    total_pages = len(reader.pages)
    split_pages = list(set([int(p)-1 for p in split_pages if 0 < int(p) <= total_pages]))

    outputs = []

    for page_num in split_pages:
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        with open(temp_file.name, "wb") as f:
            writer.write(f)

        outputs.append({
            "page": page_num + 1,
            "file_path": temp_file.name
        })

    return outputs
