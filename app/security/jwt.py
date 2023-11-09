from datetime import datetime, timedelta

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from fastapi.security import HTTPAuthorizationCredentials
from src.app.project.config import settings


oauth2_scheme = HTTPBearer()


def create_access_token(data: dict, minutes: int = settings.ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token has expired or is invalid")


def get_current_user(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    user = decode_token(token.credentials)
    return user


