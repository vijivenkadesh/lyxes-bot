from core.config import settings
from langchain_openai import ChatOpenAI
from schema.schemas import MessageState



class LyxesBot:
    OPENAI_API_KEY = settings.OPENAI_API_KEY
    MODEL = settings.MODEL
    @classmethod
    def get_llm(cls, openai_model: str= ""):
        
        if openai_model:
            return ChatOpenAI(model=openai_model, api_key=cls.OPENAI_API_KEY)
        else:
            return ChatOpenAI(model=cls.MODEL, api_key=cls.OPENAI_API_KEY )
        


def lyxes_agent_node(state: MessageState):
    try:
        agent = LyxesBot().get_llm()
    except Exception as e:
        return e
    
    if agent:
        response = agent.invoke(input=state.query)
        state.query = state.query
        state.response = str(response.content)
        return state