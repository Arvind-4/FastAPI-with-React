from datetime import (
    datetime, 
    timedelta,
)
from jose import (
    JWTError, 
    jwt,
)

from app.config import get_settings

settings = get_settings()

SECRET_KEY = settings.secret_key
ALGORITHM = settings.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.session_duration

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("payload",payload)
        username: str = payload.get("username")
        if username is None:
            raise JWTError("Invalid token")
    except JWTError:
        raise JWTError("Invalid token")