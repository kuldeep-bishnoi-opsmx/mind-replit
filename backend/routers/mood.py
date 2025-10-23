from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta

from database import get_db
from models import User, Mood as MoodModel
from schemas import MoodCreate, Mood
from services.auth_service import get_current_user
from services.ai_service import ai_service

router = APIRouter()

@router.post("/", response_model=Mood)
async def create_mood(
    mood_data: MoodCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Log a new mood entry."""
    
    sentiment_score = None
    if mood_data.notes:
        sentiment_score = ai_service.analyze_sentiment(mood_data.notes)
    
    db_mood = MoodModel(
        user_id=current_user.id,
        mood_emoji=mood_data.mood_emoji,
        mood_score=mood_data.mood_score,
        notes=mood_data.notes,
        sentiment_score=sentiment_score
    )
    
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    
    return db_mood

@router.get("/", response_model=List[Mood])
async def get_moods(
    days: int = 30,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get mood entries for the current user."""
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    
    moods = db.query(MoodModel).filter(
        MoodModel.user_id == current_user.id,
        MoodModel.date >= cutoff_date
    ).order_by(MoodModel.date.desc()).all()
    
    return moods

@router.get("/today", response_model=Mood)
async def get_today_mood(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get today's mood entry."""
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    
    mood = db.query(MoodModel).filter(
        MoodModel.user_id == current_user.id,
        MoodModel.date >= today_start
    ).first()
    
    if not mood:
        raise HTTPException(status_code=404, detail="No mood logged today")
    
    return mood
