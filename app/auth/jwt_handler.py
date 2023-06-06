import time 
import jwt 
from decouple import config

JWT_SECRET = config("secret")
JWT_ATGORITHM = config("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# Функция генерирует токены (JWTs)
def token_response(token: str):
    return{
        "access token" : token
    }

# Function used for signing the JWT strings
def signJWT(userID: str):
    payload = {
        "usedID" : userID, 
        "expiry" : time.time() + ACCESS_TOKEN_EXPIRE_MINUTES
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ATGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ATGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None 
    except:
        return {}   