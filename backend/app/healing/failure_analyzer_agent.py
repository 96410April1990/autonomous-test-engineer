import json
import os
import re

from app.services.llm_service import LLMService
from app.models.failure_report import ( FailureReport )

class FailureAnalyzerAgent:
    def __init__(self):
        self.llm = LLMService()
    
    def analyze(self, failure_log: str):
        prompt = f"""
        
        You are an expert QA Automation Engineer.

        Analyze this playwright failure.

        Identify:

        1. Error type
        2. Root cause
        3. Suggested fix
        4. Confidence level

        Return only JSON.

        Format:

        {{
            "error_type": "",
            "root_cause": "",
            "suggested_fix": "",
            "confidence": ""
        }}

        Failure:

        {failure_log}

        """

        response = self.llm.generate(prompt)
        clean = self.extract_json(response)
        data = json.loads(clean)

        return FailureReport(**data)
    
    def extract_json(self, text):
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return match.group()
        
        raise Exception("Invalid AI response")
    
    
    