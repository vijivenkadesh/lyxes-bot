from core.config import EnvSettings
def main():
    settings = EnvSettings()

    key = settings.OPENAI_API_KEY
    print(settings.OPENAI_API_KEY)
if __name__ == "__main__":
    main()