from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.firebase import init_firebase
from app.api.routes import user_routes, project_routes, join_request_routes, notification_routes
from app.utils.error_handler import register_exception_handlers

app = FastAPI(title=settings.APP_NAME)
register_exception_handlers(app)

# ✅ Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Initialize Firebase once during startup
@app.on_event("startup")
def on_startup():
    init_firebase()

# ✅ Routers
app.include_router(user_routes.router, prefix="/api", tags=["Users"])
app.include_router(project_routes.router, prefix="/api", tags=["Projects"])
app.include_router(join_request_routes.router, prefix="/api", tags=["Join Requests"])
app.include_router(notification_routes.router, prefix="/api", tags=["Notifications"])

# ✅ Root route
@app.get("/")
def root():
    return {"message": "CollabHub API is running 🚀"}
