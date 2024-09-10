# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import settings
from app.core.logging import setup_logging

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
setup_logging()

# Include API routes
app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    # Perform startup tasks (e.g., initialize database connection)
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Perform cleanup tasks
    pass
