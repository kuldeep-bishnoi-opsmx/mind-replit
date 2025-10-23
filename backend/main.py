from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
import uvicorn
from dotenv import load_dotenv
import os

from database import engine, get_db
from models import Base
from routers import auth, chat, mood, journal, tips
from services.auth_service import get_current_user

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mind Coach AI Agent",
    description="A personal mental wellness assistant with AI-driven conversations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for Replit environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(mood.router, prefix="/mood", tags=["mood"])
app.include_router(journal.router, prefix="/journal", tags=["journal"])
app.include_router(tips.router, prefix="/tips", tags=["tips"])

@app.get("/")
async def root():
    return {"message": "Mind Coach AI Agent API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
