from fastapi import FastAPI
from main import main, graph_run


app = FastAPI()


@app.get("/")
def home():
    return {"message": "welcome"}


@app.get("/query")
def llm_chat(query: str):
    respone = main(query=query)
    return respone


@app.get("/agent")
def get_agent(query: str):
    response = graph_run(query=query)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="app:app")