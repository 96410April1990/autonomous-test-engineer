from app.services.llm_service import ( LLMService )
from app.llm_gateway.cache import ( PromptCache )
from app.llm_gateway.retry_handler import ( RetryHandler )

class LLMGateway:
    def __init__(self):
        self.llm = LLMService()
        self.cache = PromptCache()
        self.retry = RetryHandler()

    def generate(self, prompt):
        cached = (self.cache.get(prompt))
        if cached:
            return cached
        response = self.retry.execute(lambda: self.llm.generate(prompt))
        self.cache.save(prompt, response)

        return response