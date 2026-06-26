import json
import os
import re
from app.services.llm_service import LLMService
from app.models.test_suite import ( TestSuite )

class TestArchitectAgent:

    def __init__(self):
        self.llm = LLMService()

    def generate_tests(self, requirement_json: str):
        prompt = f"""
        You are a Senior QA Architect.

        Generate exhaustive test cases.

        Include:

        1. Positive scenarios
        2. Negative scenarios
        3. Edge cases
        4. Boundary cases

        Return ONLY JSON.

        Format:

        {{
            "feature_name": "",
            "test_cases": [
                "test_id": "",
                "title": "",
                "test_type": "",
                "priority": "",
                "steps": [
                    {{
                        "step_number": 1,
                        "action": "",
                        "expected_result": ""
                    }}
                ]
            ]
        }}

        Requirement:

        {requirement_json}

        """

        response = self.llm.generate(prompt)

        clean = self.extract_json(response)

        try:
            data = json.loads(clean)
        except json.JSONDecodeError:
            clean = clean.replace("\\", "\\\\")
            data = json.loads(clean)
            
        return TestSuite(**data)
    
    def extract_json(self, text: str):
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return match.group()
        
        raise Exception("Invalid AI response.")
    
