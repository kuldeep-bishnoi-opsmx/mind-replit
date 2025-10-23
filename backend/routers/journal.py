from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User, JournalEntry as JournalEntryModel
from schemas import JournalEntryCreate, JournalEntryUpdate, JournalEntry
from services.auth_service import get_current_user
from services.ai_service import ai_service

router = APIRouter()

@router.post("/", response_model=JournalEntry)
async def create_journal_entry(
    entry_data: JournalEntryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new journal entry."""
    
    sentiment_score = ai_service.analyze_sentiment(entry_data.content)
    
    db_entry = JournalEntryModel(
        user_id=current_user.id,
        title=entry_data.title,
        content=entry_data.content,
        ai_prompt=entry_data.ai_prompt,
        sentiment_score=sentiment_score
    )
    
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    
    return db_entry

@router.get("/", response_model=List[JournalEntry])
async def get_journal_entries(
    limit: int = 10,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get journal entries for the current user."""
    entries = db.query(JournalEntryModel).filter(
        JournalEntryModel.user_id == current_user.id
    ).order_by(JournalEntryModel.created_at.desc()).limit(limit).all()
    
    return entries

@router.get("/{entry_id}", response_model=JournalEntry)
async def get_journal_entry(
    entry_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific journal entry."""
    entry = db.query(JournalEntryModel).filter(
        JournalEntryModel.id == entry_id,
        JournalEntryModel.user_id == current_user.id
    ).first()
    
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    
    return entry

@router.put("/{entry_id}", response_model=JournalEntry)
async def update_journal_entry(
    entry_id: int,
    entry_data: JournalEntryUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a journal entry."""
    entry = db.query(JournalEntryModel).filter(
        JournalEntryModel.id == entry_id,
        JournalEntryModel.user_id == current_user.id
    ).first()
    
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    
    if entry_data.title is not None:
        entry.title = entry_data.title
    if entry_data.content is not None:
        entry.content = entry_data.content
        entry.sentiment_score = ai_service.analyze_sentiment(entry_data.content)
    
    db.commit()
    db.refresh(entry)
    
    return entry

@router.delete("/{entry_id}")
async def delete_journal_entry(
    entry_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a journal entry."""
    entry = db.query(JournalEntryModel).filter(
        JournalEntryModel.id == entry_id,
        JournalEntryModel.user_id == current_user.id
    ).first()
    
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    
    db.delete(entry)
    db.commit()
    
    return {"message": "Journal entry deleted successfully"}

@router.get("/prompt/generate")
async def generate_journal_prompt(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate an AI-powered journal prompt."""
    prompt = ai_service.generate_journal_prompt()
    
    return {"prompt": prompt}
