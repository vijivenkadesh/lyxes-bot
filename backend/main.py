from agents.lxyes_bot import LyxesBot
def main():
    llm = LyxesBot.get_llm(openai_model="gpt-4.1-nano")
    response = llm.invoke("Hello How are you")
    print(response)

if __name__ == "__main__":
    main()