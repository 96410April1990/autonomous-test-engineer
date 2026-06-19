#from openai import OpenAI
import google.generativeai as genai
from app.core.config import settings

class LLMService:
    # def __init__(self):
    #     self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    # def generate(self, prompt: str):
    #     response = self.client.chat.completions.create(
    #         model="gemini-2.5-flash-lite",
    #         messages=[
    #             {
    #                 "role":"user",
    #                 "content":prompt
    #             }
    #         ]
    #     )
    #     return (response.choices[0].message.content)
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite")

    def generate(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text