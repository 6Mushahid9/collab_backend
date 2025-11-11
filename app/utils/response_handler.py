# app/utils/response_handler.py
from fastapi.responses import JSONResponse

def success_response(data=None, message: str = "Success", status_code: int = 200):
    """Standardized success response."""
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data or {}
        }
    )

def error_response(message: str = "Error", status_code: int = 400, payload=None):
    """Standardized manual error response (use AppError for automatic)."""
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": message,
            "payload": payload or {}
        }
    )
