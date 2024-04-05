from fastapi import FastAPI, HTTPException
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

@app.post("/generate-password")
def generate_password(pass_args: Pass_Args):
    # Error Handling
    if (pass_args.length > 60 or pass_args.length < 8):
        raise HTTPException(
                status_code=400,
                detail="length argument must be between 8 and 60"
            )

    password = new_password.generate_password(pass_args.length, pass_args.capitals, pass_args.digits, pass_args.symbols)
    return {"password": password, "password_length": len(password)}