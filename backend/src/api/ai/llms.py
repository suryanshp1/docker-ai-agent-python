import os
from langchain_openai import ChatOpenAI


OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_MODEL_NAME = os.getenv("OPENAI_API_MODEL_NAME", "gpt-4o-mini")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")
if not OPENAI_API_MODEL_NAME:
    raise ValueError("OPENAI_API_MODEL_NAME is not set")
if not OPENAI_BASE_URL:
    raise ValueError("OPENAI_BASE_URL is not set")

def get_openai_llm():
    openai_params = {
        "model_name": OPENAI_API_MODEL_NAME,
        "api_key": OPENAI_API_KEY,
        "base_url": OPENAI_BASE_URL,
    }

    llm_base = ChatOpenAI(**openai_params)

    return llm_base
