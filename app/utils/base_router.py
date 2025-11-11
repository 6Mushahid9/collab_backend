from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from typing import Callable
from app.utils.response_handler import success_response, error_response


class BaseRoute(APIRoute):
    """Custom route wrapper to standardize responses."""

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request):
            try:
                response = await original_route_handler(request)

                # If route already returned a JSONResponse (custom), return as-is
                if isinstance(response, JSONResponse):
                    return response

                # Otherwise wrap in standard success response
                return success_response(response)

            except Exception as e:
                # Standardize uncaught errors
                return error_response(str(e), status_code=500)

        return custom_route_handler


class BaseRouter(APIRouter):
    """Router that automatically applies standardized responses."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.route_class = BaseRoute
