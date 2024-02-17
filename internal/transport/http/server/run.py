from fastapi import FastAPI
from package.config import Config
import uvicorn


def Run(server: FastAPI, config: Config):
    """ Run function is used to start the FastAPI server

    Args:
        server (FastAPI): server.Application: FastAPI application instance
        config (Config): package.config.Config: Config instance
    """

    uvicorn.run(server, host=config.app_host, port=config.app_port)
