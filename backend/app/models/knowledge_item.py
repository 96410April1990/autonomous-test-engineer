from pydantic import BaseModel

class KnowledgeItem(BaseModel):
    issue:str
    solution:str
    category:str
    source:str


