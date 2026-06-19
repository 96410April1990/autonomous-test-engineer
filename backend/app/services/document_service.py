import os

from app.parsers.pdf_parser import PDFParser
from app.parsers.docx_parser import DOCXParser
from app.parsers.text_parser import TextParser

class DocumentService:

    def __init__(self):
        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.text_parser = TextParser()

    def process_document(self, file_path: str):
        extension = (os.path.splitext(file_path)[1].lower())
        if extension == ".pdf":
            return self.pdf_parser.extract_text(file_path)
        elif extension == ".docx":
            return self.docx_parser.extract_text(file_path)
        elif extension == ".txt":
            return self.text_parser.extract_text(file_path)
        else:
            raise Exception("Unsupported file type")
    
    
