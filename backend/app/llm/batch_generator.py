import json
import re
from app.services.llm_service import ( LLMService )

class BatchPlayWrightGenerator:
    def __init__(self):
        self.llm = LLMService()

    def generate(self, test_cases:list):
        if not test_cases:
            raise Exception("No test cases received from Test Architect Agent")
        prompt = f"""
        You are an expert Playwright Python Automation Engineer.

        Generate Playwright pytest tests for ALL test cases below.

        Rules:

        1. Use Python Playwright
        2. Use pytest
        3. Create independent tests
        4. Use best practices
        5. Add comments
        6. Return ONLY JSON

        Format:

        {{
        "files":[
        {{
        "file_name":"test_name.py",
        "code":"python code"
        }}
        ]
        }}

        Test Cases:

        {json.dumps(
            [
                test
                for test in test_cases
            ],
            indent=2
        )}

        """

        response = self.llm.generate(prompt)

        return self.extract_json(response)
    
    def extract_json(self, text):
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise Exception("Invalid Gemini response")