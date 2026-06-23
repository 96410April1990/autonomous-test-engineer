from pydantic import BaseModel
from typing import List

class TestStep(BaseModel):
    step_number: int
    action: str
    expected_result: str

class GeneratedTestCase(BaseModel):
    test_id: str
    title: str
    test_type: str
    priority: str
    steps: List[TestStep]

class TestSuite(BaseModel):
    feature_name: str
    test_cases: List[GeneratedTestCase]

