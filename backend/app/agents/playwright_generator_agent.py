import re
from app.services.llm_service import LLMService
from app.automation.playwright_template import ( PLAYWRIGHT_TEMPLATE )

class PlaywrightGeneratorAgent:

    def __init__(self):
        self.llm = LLMService()

    def generate_code(self, test_case: str):
        prompt = f"""
        You are a python playwright expert.

        Convert this test case into pytest playwright code.

        Rules:

        - Use playwright.sync_api
        - Use readable locators
        - Add assertions
        - Return only python code

        Test Case:

        {test_case}

        """

        code = self.llm.generate(prompt)

        return self.clean_code(code)
    
    def clean_code(self, code: str):
        code = re.sub(r"```python", "", code)
        code = code.replace("```", "")

        return code.strip()
    
    

