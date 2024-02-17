from fastapi import FastAPI
from internal.transport import handlers as h


def NewRouter(app: FastAPI) -> FastAPI:
    """ NewRouter function is used to create a router for the application

    Args:
        app (FastAPI): server.Application: FastAPI application instance

    Returns:
        FastAPI:  server.Application with joined router
    """
    router = FastAPI()

    router.get("/ping")(h.Pong)

    app.mount("/api", router)

    return app
