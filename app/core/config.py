from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AMC Chatbot API"

    # Security
    API_KEY_NAME: str = "X-API-Key"
    API_KEY: str

    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]

    # OpenAI Configuration
    OPENAI_API_KEY: str
    GPT_MODEL: str = "gpt-4"
    MAX_TOKENS: int = 1000
    TEMPERATURE: float = 0.7

    # Pinecone Configuration
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")

    # Namespace Configuration
    NAMESPACE_MAP: dict = {
        "GPMC Act": "gpmcact",
        "Compilation of Circulars": "compcirculars",
        "Tax Laws": "taxlaw"
    }

    class Config:
        env_file = ".env"

settings = Settings()
