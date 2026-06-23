from pydantic import BaseModel
from typing import List

class TestFailure(BaseModel):
    test_name: str
    error: str

class ExecutionResult(BaseModel):
    total_tests: int
    passed: int
    failed: int
    duration: float
    failures: List[TestFailure]
