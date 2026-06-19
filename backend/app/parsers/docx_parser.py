from docx import Document

class DOCXParser:

    def extract_text(self, file_path: str):
        document = Document(
            file_path
        )

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

