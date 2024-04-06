from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from PIL import Image
import passwordGenerator.passwordGenerator as new_password
import requests

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
    request_url = "https://dog.ceo/api/breeds/list/all"
    try:
        request_return = requests.get(request_url).json()
        return request_return
    except requests.exceptions.RequestException as e:
        return {"message": "An exception has occured", "status": "error"}

@app.get("/dog-picture")
def dog_picture(breed: str=None, sub_breed: str=None):
    request_url = "https://dog.ceo/api/breeds/image/random"
    if (not sub_breed and breed):
        request_url = "https://dog.ceo/api/breed/{0}/images/random".format(breed)
    if (sub_breed and breed):
        request_url = "https://dog.ceo/api/breed/{0}/{1}/images/random".format(breed, sub_breed)

    # get url of random image
    try:
        request_return = requests.get(request_url).json()
        image_url = request_return["message"]
        data = "<!DOCTYPE html><html><body><img src='{0}' alt='{0}'></body></html>".format(image_url)
        return Response(content=data)
    except requests.exceptions.RequestException as e:
        return {"message": "An exception has occured", "status": "error"}