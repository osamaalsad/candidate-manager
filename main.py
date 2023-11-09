import uvicorn
from fastapi import FastAPI
from app.routers import candidate, generate_report
from app.routers import health, user
from app.security import auth

app = FastAPI()

app.include_router(health.router, tags=["health-check"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(candidate.router, prefix="/candidate", tags=["candidate"])
app.include_router(generate_report.router, prefix="/generate-report", tags=["generate-report"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)