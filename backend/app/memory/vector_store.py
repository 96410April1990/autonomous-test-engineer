from typing import List
from app.models.knowledge_item import ( KnowledgeItem )

class VectorStore:

    def __init__(self):
        self.items:List[KnowledgeItem] = []

    def add(self, item:KnowledgeItem):
        self.items.append(item)

    def search(self, query:str):
        results = []
        for item in self.items:
            if (query.lower() in item.issue.lower()):
                results.append(item)
        
        return results
    
    