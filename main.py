from internal.transport.http.server import server
from package.config import NewConfig
import sys
import os


def main():
    """ main function is used to start the FastAPI server
    """

    config = NewConfig()
    app = server.NewServer(config)
    app.Run()


def debug():
    """ debug function is used to start the FastAPI server in debug mode
    """
    os.environ["app_name"] = "FastAPI"
    os.environ["app_host"] = "localhost"
    os.environ["app_port"] = "8000"
    os.environ["app_debug"] = "True"
    os.environ["postgres_host"] = "localhost"
    os.environ["postgres_port"] = "5432"
    os.environ["postgres_user"] = "postgres"
    os.environ["postgres_password"] = "postgres"
    os.environ["postgres_db"] = "postgres"

    config = NewConfig()
    app = server.NewServer(config)
    app.Run()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        main()
    if sys.argv[1] == "debug":
        debug()
    else:
        main()
