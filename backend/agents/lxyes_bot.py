from langchain_openai import ChatOpenAI
from core.config import EnvSettings





class LyxesBot:
    settings = EnvSettings()
    OPENAI_API_KEY = settings.OPENAI_API_KEY
    MODEL = settings.MODEL

    @classmethod
    def get_llm(cls, openai_model: str):
        if openai_model:
            return ChatOpenAI(model=openai_model, api_key=cls.OPENAI_API_KEY)
        else:
            return ChatOpenAI(model=cls.MODEL, api_key=cls.OPENAI_API_KEY )