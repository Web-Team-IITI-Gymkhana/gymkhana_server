from pydantic import BaseSettings, EmailStr, HttpUrl, PostgresDsn


class Settings(BaseSettings):
    TITLE: str = "Gymkhana Server"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend for the Gymkhana Server"

    NAME: str = "IIT INDORE"
    URL: HttpUrl = "https://www.iiti.ac.in/"
    EMAIL: EmailStr = "AakashGupta@iiti.ac.in"

    LICENSE_NAME: str = "MIT"
    LICENSE_URL: HttpUrl = (
        "https://github.com/Web-Team-IITI-Gymkhana/gymkhana_server/blob/main/LICENSE"
    )

    PGUSER: str
    PGPASSWORD: str
    PGHOST: str
    PGDATABASE: str
    PGPORT: int

    SECRET_KEY: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    FRONTEND_URL: str
    ENVIRONMENT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "UTF-8"

    def get_connection_string(self) -> PostgresDsn:
        return f"postgresql://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"

    def debug(self) -> bool:
        return self.ENVIRONMENT == "DEVELOPMENT"


settings = Settings()
