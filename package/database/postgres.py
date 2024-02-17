"""
File to create the connection to the database
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from package.config import Settings

Base = None
Session = None

config = Settings()

engine = create_engine(
    f"postgresql://{config.postgres_user}:{config.postgres_password}" +
    f"@{config.postgres_host}:{config.postgres_port}/{config.postgres_db}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
