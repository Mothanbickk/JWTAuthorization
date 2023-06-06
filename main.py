from fastapi import FastAPI, Body, Depends
import uvicorn
from app.model import UserSchema, UserLoginSchema 
from app.auth.jwt_handler import signJWT
from app.auth.jwt_berear import jwtBearer

app = FastAPI()

#1
@app.get("/", tags=["test"])
def greet():
    return {"hello":"Askar!"}

# User SignUp [Create a new user]
@app.post("/signup", tags = ["About User"])
def create_user(user: UserSchema=Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == user.email and user.password == user.password:
            return True
        return False

# User Login 
@app.post("/login", tags = ["About User"])
def user_login(user: UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error" : "Invalid login details!"
        }
    
users = []