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

@app.get("/",
    responses = {
        200: {
            "content": {"application/json": {
                "example": '{"hello":"world"}'
            }}
        }
    })
def read_root():
    return {"Hello": "World"}

@app.post("/generate-password",
    responses = {
        200: {
            "content": {"application/json": {
                "example": '{"password": "cbbolxaqho", "password_length": 10, "status": "success"}'
            }}
        },
        422: {
            "content": {"application/json": {
                "example": '{"detail": [{"type": "int_parsing", "loc": ["body","length"],"msg": "Input should be a valid integer, unable to parse string as an integer", "input": "avocado", "url": "https://errors.pydantic.dev/2.6/v/int_parsing"}]}'
            }}
        }
    })
def generate_password(pass_args: Pass_Args):
    # Error Handling
    if (pass_args.length > 60 or pass_args.length < 8):
        raise HTTPException(
                status_code=400,
                detail="length argument must be between 8 and 60"
            )

    password = new_password.generate_password(pass_args.length, pass_args.capitals, pass_args.digits, pass_args.symbols)
    return {"password": password, "password_length": len(password), "status": "success"}

@app.get("/dog-breed-list",
    responses = {
        200: {
            "content": {"application/json": {
                "example": '{"message":{"affenpinscher":[],"african":[],"airedale":[],"akita":[],"appenzeller":[],"australian":["shepherd"],..."status":"success"}'
            }}
        },
        400: {
            "content": {"application/json": {
                "example": '{"message": "An exception has occured", "status": "error"}'
            }}
        }
    })
def dog_breed_list():
    return dog.dog_breed_list()

@app.get("/dog-picture", 
    responses = {
        200: {
            "content": {"application/html": {
                "example": "<html><head></head><body><img src='https://images.dog.ceo/breeds/terrier-russell/iguet2.jpg' alt='https://images.dog.ceo/breeds/terrier-russell/iguet2.jpg'></body></html>"
            }},
            "description": "Returns a html document with an image tag with a source pointing to an image"
        },
        400: {
            "content": {"application/json": {
                "example": '{"message": "An exception has occured", "status": "error"}'
            }}
        },
        404: {
            "content": {"application/html": {
                "example": "<html><head></head><body><img src='' alt='Breed not found (sub breed does not exist)'></body></html>"
            },
            "description": "Returns a html document with an image tag with no source and alt text explaining the problem with the request"}
        }
    },
    
    response_class=Response)
def dog_picture(breed: str=None, sub_breed: str=None):
    return dog.dog_picture(breed, sub_breed)