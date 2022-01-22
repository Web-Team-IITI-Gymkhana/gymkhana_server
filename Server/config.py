import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TITLE = "Gymkhana Server"
    VERSION = "1.0.0"
    DESCRIPTION = "Backend for the Gymkhana Server"

    NAME = "IIT INDORE"
    URL = "https://www.iiti.ac.in/"
    EMAIL = "AakashGupta@iiti.ac.in"

    LICENSE_NAME = "MIT"
    LICENSE_URL = "https://github.com/Web-Team-IITI-Gymkhana/gymkhana_server/blob/main/LICENSE"

    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE = os.getenv("DATABASE")
    CONNECTION_STRING = (
        f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@localhost/{DATABASE}"
    )
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    DEBUG = os.getenv("IN") == "DEVELOPMENT"


settings = Settings()
