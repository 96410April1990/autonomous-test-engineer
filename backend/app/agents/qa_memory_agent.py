from app.memory.knowledge_service import ( KnowledgeService )

class QAMemoryAgent:
    
    def __init__(self):
        self.memory = KnowledgeService()

    def remember(self, issue, solution):
        from app.models.knowledge_item import ( KnowledgeItem )
        item = KnowledgeItem(issue=issue, solution=solution, category="automation", source="AI")
        return self.memory.save(item)
    
    def recall(self, query):
        return self.memory.search(query)
    
    

