from fastapi import FastAPI
from internal.transport.http.router import NewRouter
from package.config import Config
import uvicorn


class Server(FastAPI):
    server_host: str
    server_port: int

    def __init__(self, **kwargs):
        """ __init__ function is used to initialize the FastAPI server
        """

        server_host = kwargs.get("server_host", -1)
        server_port = kwargs.get("server_port", -1)

        if server_host == -1 or server_port == -1:
            raise ValueError("server host and port is required")

        super().__init__()

        self.server_host = server_host
        self.server_port = server_port

    def Run(self):
        """ Run function is used to start the FastAPI server
        """
        uvicorn.run(self, host=self.server_host, port=self.server_port)


def NewServer(config: Config) -> Server:
    """ NewServer function is used to create a new FastAPI server instance

    Returns:
        FastAPI: server.Application: FastAPI application instance
    """

    app = Server(
        server_host=config.app_host,
        server_port=config.app_port,
    )

    # Join router to the application
    app = NewRouter(app)

    return app
