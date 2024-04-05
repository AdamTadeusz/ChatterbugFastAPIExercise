from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import passwordGenerator.passwordGenerator as new_password

class Pass_Args(BaseModel):
    length: int = 20
    capitals: bool = True
    digits: bool = True
    symbols: bool = True

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/generate-password")
def generate_password(pass_args: Pass_Args):
    password = new_password.generate_password(pass_args.length, pass_args.capitals, pass_args.digits, pass_args.symbols)
    return {"password": password, "password_length": len(password)}