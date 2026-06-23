from app.memory.vector_store import ( VectorStore )
from app.models.knowledge_item import ( KnowledgeItem )

class KnowledgeService:

    def __init__(self):
        self.store = VectorStore()

    def save(self, item:KnowledgeItem):
        self.store.add(item)
        return { "status":"saved" }
    
    def search(self, query:str):
        return self.store.search(query)
    