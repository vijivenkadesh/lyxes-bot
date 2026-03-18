from pydantic import BaseModel, Field



class MessageState(BaseModel):
    user: str = Field(description="This field reprents the user name for the current session", default="")
    query: str = Field(description="This is the user query or question asked to the custom chatbot", default="")
    response: str = Field(description="This is bot response for the user query or question")