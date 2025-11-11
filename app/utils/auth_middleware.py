from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.firebase import verify_firebase_token

auth_scheme = HTTPBearer()

async def firebase_auth(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    """Dependency for verifying Firebase tokens in protected routes."""
    try:
        decoded_token = verify_firebase_token(token.credentials)
        return decoded_token
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
