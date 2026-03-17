from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field



class EnvSettings(BaseSettings):
    OPENAI_API_KEY: str = Field(description="This is an API key for openai", default="")
    LANGSMITH_TRACING: bool = True
    LANGSMITH_ENDPOINT: str = ""
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_PROJECT: str = ""




    model_config = SettingsConfigDict(env_file=".env",
                                env_file_encoding="utf-8",
                                case_sensitive=True)