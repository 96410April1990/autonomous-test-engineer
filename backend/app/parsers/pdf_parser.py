from pypdf import PdfReader

class PDFParser:

    def extract_text(self, file_path: str):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        return text

