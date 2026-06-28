import json
import os
import re
from app.services.llm_service import LLMService
from app.models.test_suite import ( TestSuite )
from app.rag.rag_service import RAGService
from app.guardrails.qa_guardrails import ( QAGuardrail )

class TestArchitectAgent:

    def __init__(self):
        self.llm = LLMService()
        self.guardrail = QAGuardrail()
        self.rag = RAGService()

    def generate_tests(self, requirement_json: str):
        if not self.guardrail.validate_input(requirement_json):
            print("======== GUARDRAIL RESULT ========")
            print(requirement_json)
            print("==================================")
            raise Exception("Requirement Rejected")
        context = self.rag.retrieve(requirement_json)
        prompt = f"""
        You are an AI QA Engineer.

        Generate exhaustive test cases.

        Include:

        1. Positive scenarios
        2. Negative scenarios
        3. Edge cases
        4. Boundary cases

        Return ONLY JSON.

        The root key must be:
        test_cases

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

        Use this existing knowledge:

        {context}

        Requirement:

        {requirement_json}

        """

        response = self.llm.generate(prompt)

        clean = self.extract_json(response)

        try:
            data = json.loads(clean)
            if "test_cases" not in data:
                raise Exception(
                    f"Invalid Test Architect response: {data}"
                )
        except json.JSONDecodeError:
            #clean = clean.replace("\\", "\\\\")
            data = json.loads(clean)
            if "test_cases" not in data:
                raise Exception(
                    f"Invalid Test Architect response: {data}"
                )
            
        print("======== TEST SUITE GENERATED ========")
        print(json.dumps(data, indent=2))
        print("======================================")
        suite = TestSuite(**data)

        print("======== TEST ARCHITECT RETURN ========")
        print(type(suite))
        print(suite)
        print("========================================")

        return suite
    
    def extract_json(self, text: str):
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return match.group()
        
        raise Exception("Invalid AI response.")
    
