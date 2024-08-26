from fastapi import FastAPI

def add_root_route(app: FastAPI):
    @app.get("/")
    def root():
        return {"message": "Service is working"}