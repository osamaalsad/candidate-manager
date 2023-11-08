from fastapi import FastAPI
from app.routers import health, user, candidate, generate_report
from app.security import auth

app = FastAPI()

app.include_router(health.router)
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(candidate.router, prefix="/candidate", tags=["candidate"])
app.include_router(generate_report.router, prefix="/generate-report", tags=["generate-report"])
