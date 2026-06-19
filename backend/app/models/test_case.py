from pydantic import BaseModel
from typing import List

class TestStep(BaseModel):

    step_number: int
    action: str
    expected_result: str

class TestCase(BaseModel):

    test_id: str
    title: str
    test_type: str
    priority: str
    steps: List[TestStep]
