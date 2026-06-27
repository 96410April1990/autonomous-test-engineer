import chromadb

class VectorStore:
    def __init__(self):
        self.client = (chromadb.Client())
        self.collection = (self.client.get_or_create_collection("qa_docs"))

    def add_document(self, text, id):
        self.collection.add(documents=[text], ids=[id])

    def search(self, query):
        result = (self.collection.query(query_texts=[query], n_results=3))
        return result["documents"][0]