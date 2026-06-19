from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./vector_db")

settings = Settings()

