from pydantic import BaseModel

class FailureReport(BaseModel):
    error_type:str
    root_cause:str
    suggested_fix:str
    confidence:str

    
