"""
config.py created for importing the settings from the .env file


"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Define the settings
    app_name: str # Name of the application
    app_host: str # Host of the application
    app_port: int # Port of the application
    app_debug: bool # Debug mode of the application

    postgres_host: str # Host of the postgres database
    postgres_port: int # Port of the postgres database
    postgres_user: str # User of the postgres database
    postgres_password: str # Password of the postgres database
    postgres_db: str # Database name of the postgres database



    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=('.env', '.env.prod')
    )


def ImportConfig():
    return Settings()

