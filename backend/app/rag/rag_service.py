import os
from app.vector.vector_store import ( VectorStore )

class RAGService:
    def __init__(self):
        self.path = "app/rag/documents"
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.store = VectorStore()
        self.load_documents()
        
    def load_documents(self):
        path = "knowledge"
        for file in os.listdir(path):
            with open(os.path.join(path, file)) as f:
                self.store.add_document(f.read(), file)

    def retrieve(self, query):
        context = []
        for file in os.listdir(self.path):
            full_path = os.path.join(self.path, file)
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                if any(word.lower() in content.lower() for word in query.split()):
                    context.append(content)

        return "\n".join(context)
    

        