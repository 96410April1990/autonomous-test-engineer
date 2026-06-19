from pydantic import BaseModel
from typing import List

class Requirement(BaseModel):

    feature_name: str
    actors: List[str]
    acceptance_criteria: List[str]
    business_rules: List[str]
