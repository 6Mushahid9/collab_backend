from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.firebase import init_firebase
from app.api.routes.user_routes import router as user_router

app = FastAPI(title=settings.APP_NAME)

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
    print("🔥 Firebase ready and connected!")

# ✅ Routers
app.include_router(user_router, prefix="/api", tags=["Users"])

# ✅ Root route
@app.get("/")
def root():
    return {"message": "CollabHub API is running 🚀"}
