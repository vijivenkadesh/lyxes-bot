from agents.lxyes_bot import LyxesBot, lyxes_agent_node
from langgraph.graph import StateGraph, START, END
from schema.schemas import MessageState

def main(query: str):
    llm = LyxesBot.get_llm(openai_model="gpt-4.1-nano")
    response = llm.invoke(input=query)
    return response.content


graph = StateGraph(state_schema=MessageState)

graph.add_node(node=lyxes_agent_node)
graph.add_edge(start_key=START, end_key="lyxes_agent_node")
graph.add_edge(start_key="lyxes_agent_node", end_key=END)
app = graph.compile()

def graph_run(query: str):
    input = MessageState()
    input.query = query
    response = app.invoke(input=input)
    return response

if __name__ == "__main__":
    graph_run(query="What is the weather in Bangalore")


