from app.memory.knowledge_service import ( KnowledgeService )
from app.models.knowledge_item import ( KnowledgeItem )

class QAMemoryAgent:
    
    def __init__(self):
        self.memory = KnowledgeService()

    def remember(self, issue:str, solution:str):
        item = KnowledgeItem(issue=issue, solution=solution, category="automation", source="AI")
        return self.memory.save(item)
    
    def recall(self, query:str):
        return self.memory.search(query)
    
    

