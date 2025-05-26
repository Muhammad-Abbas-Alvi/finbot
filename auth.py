from fastapi import Header, HTTPException, status

token_db = {"user-token": "finance123"}

def authenticate_user(authorization: str = Header(...)):
    if authorization not in token_db.values():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return authorization
