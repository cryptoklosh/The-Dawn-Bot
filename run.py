import asyncio
import sys
import os

from application import ApplicationManager
from utils import setup
from prometheus_client import start_http_server


def main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    setup()
    start_http_server(8080)
    app = ApplicationManager(sys.argv)
    x = asyncio.run(app.run())
    os._exit(0)


if __name__ == "__main__":
    main()
