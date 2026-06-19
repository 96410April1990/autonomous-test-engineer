import json
import re
from app.services.llm_service import LLMService
from app.models.requirement import Requirement

class RequirementAnalyzerAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, requirement_text: str):
        prompt = f"""
        You are an expert QA Engineer. 

        Analyze this requirement.

        Extract:

        - feature_name
        - actors
        - acceptance_criteria
        - business_rules

        Return ONLY JSON.
        Do not add markdown.
        Do not add explanations.

        Example format:

        {{
        "feature_name":"Login",
        "actors":["Customer"],
        "acceptance_criteria":["User can login"],
        "business_rules":["Password required"]
        }}

        Requirement:

        {requirement_text}
        """

        result = self.llm.generate(prompt)
        cleaned_json = self.extract_json(result)
        data = json.loads(cleaned_json)

        return Requirement(**data)

    def extract_json(self, text: str):
        match = re.search(r"\{.*\}",text,re.DOTALL)
        if match:
            return match.group()
        
        raise Exception("The LLM did not return a valid JSON.")
