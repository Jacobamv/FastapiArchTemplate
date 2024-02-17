"""
config.py created for importing the settings from the .env file


"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Define the settings

    # Name of the application
    app_name: str

    # Host of the application
    app_host: str

    # Port of the application
    app_port: int

    # Debug mode of the application
    app_debug: bool

    # Host of the postgres database
    postgres_host: str

    # Port of the postgres database
    postgres_port: int

    # User of the postgres database
    postgres_user: str

    # Password of the postgres database
    postgres_password: str

    # Database name of the postgres database
    postgres_db: str

    # Define the settings configuration
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=('.env', '.env.prod')
    )


def NewConfig() -> Config:
    """ NewConfig function is used to create a new Config instance

    Returns:
        Config: Config instance
    """
    return Config()
