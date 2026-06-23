from app.services.llm_service import LLMService

class LocatorHealer:
    def __init__(self):
        self.llm = LLMService()

    def heal(self, failed_code:str, error:str):
        prompt = f"""

        You are a playwright expert.

        Fix this locator issue.

        Code:

        {failed_code}

        Error:

        {error}

        Return corrected python code only.

        """
        return self.llm.generate(prompt)
    
