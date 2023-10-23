import uvicorn

from fastapi import FastAPI

from auth.views.register import register_router


class Main:
    def __init__(self):
        self.app = FastAPI()

        self.app.add_route(path="/register", route=register_router)

    def run(self):
        pass

    def asgi(self):
        uvicorn.run(self.app, host="localhost", port=8080)


if __name__ == "__main__":
    Main().asgi()
