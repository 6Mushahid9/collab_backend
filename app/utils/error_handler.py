# app/core/exceptions.py
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from pydantic import BaseModel

class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400, payload: dict | None = None):
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

def register_exception_handlers(app):
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": exc.message,
                "payload": exc.payload
            }
        )

    # Optional: convert HTTPException to same structure
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": exc.detail
            }
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": "Internal Server Error",
                "details": str(exc)
            }
        )