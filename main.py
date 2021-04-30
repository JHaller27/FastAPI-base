from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="FastAPI Testing")

class AliveResponse(BaseModel):
    alive: bool


@app.get("/", response_model=AliveResponse)
def home_controller():
    return AliveResponse(alive=True)
