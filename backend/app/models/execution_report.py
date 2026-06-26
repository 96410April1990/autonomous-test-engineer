from pydantic import BaseModel
from typing import List

class ExecutionReport(BaseModel):
    feature:str
    tests_generated:int
    tests_passed:int
    tests_failed:int
    issues_found:List[str]

