from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pydantic import SecretStr
import os 



class EnvSettings(BaseSettings):
    OPENAI_API_KEY: SecretStr | None = None
    LANGSMITH_TRACING: str = "true"
    LANGSMITH_ENDPOINT: str = ""
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_PROJECT: str = ""
    MODEL: str = ""




    model_config = SettingsConfigDict(env_file=".env",
                                env_file_encoding="utf-8",
                                case_sensitive=True)
    

    def load_langsmith(self):
        os.environ['LANGSMITH_TRACING'] = self.LANGSMITH_TRACING
        os.environ['LANGSMITH_ENDPOINT'] = self.LANGSMITH_ENDPOINT
        os.environ['LANGSMITH_API_KEY'] = self.LANGSMITH_API_KEY
        os.environ['LANGSMITH_PROJECT'] = self.LANGSMITH_PROJECT



settings = EnvSettings()
settings.load_langsmith()