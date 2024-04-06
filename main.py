from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
import requests
import passwordGenerator.passwordGenerator as new_password
import dogAPI.dog as dog

class Pass_Args(BaseModel):
    length: int = 20
    capitals: bool = True
    digits: bool = True
    symbols: bool = True

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate-password")
def generate_password(pass_args: Pass_Args):
    # Error Handling
    if (pass_args.length > 60 or pass_args.length < 8):
        raise HTTPException(
                status_code=400,
                detail="length argument must be between 8 and 60"
            )

    password = new_password.generate_password(pass_args.length, pass_args.capitals, pass_args.digits, pass_args.symbols)
    return {"password": password, "password_length": len(password), "status": "success"}

@app.get("/dog-breed-list")
def dog_breed_list():
    return dog.dog_breed_list()

@app.get("/dog-picture")
def dog_picture(breed: str=None, sub_breed: str=None):
    return dog.dog_picture(breed, sub_breed)