from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pydantic import SecretStr



class EnvSettings(BaseSettings):
    OPENAI_API_KEY: SecretStr | None = None
    LANGSMITH_TRACING: bool = True
    LANGSMITH_ENDPOINT: str = ""
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_PROJECT: str = ""
    MODEL: str = ""




    model_config = SettingsConfigDict(env_file=".env",
                                env_file_encoding="utf-8",
                                case_sensitive=True)