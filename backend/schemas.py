from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Mood schemas
class MoodBase(BaseModel):
    mood_emoji: str
    mood_score: float
    notes: Optional[str] = None

class MoodCreate(MoodBase):
    pass

class Mood(MoodBase):
    id: int
    user_id: int
    sentiment_score: Optional[float] = None
    date: datetime
    
    class Config:
        from_attributes = True

# Journal schemas
class JournalEntryBase(BaseModel):
    title: str
    content: str

class JournalEntryCreate(JournalEntryBase):
    ai_prompt: Optional[str] = None

class JournalEntryUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class JournalEntry(JournalEntryBase):
    id: int
    user_id: int
    ai_prompt: Optional[str] = None
    sentiment_score: Optional[float] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Chat schemas
class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[int] = None

class ChatResponse(BaseModel):
    response: str
    session_id: int

class ChatSession(BaseModel):
    id: int
    user_id: int
    session_title: Optional[str] = None
    created_at: datetime
    messages: List[ChatMessage] = []
    
    class Config:
        from_attributes = True

# Wellness tip schemas
class WellnessTipBase(BaseModel):
    title: str
    content: str
    category: Optional[str] = None

class WellnessTipCreate(WellnessTipBase):
    pass

class WellnessTip(WellnessTipBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Dashboard schema
class DashboardData(BaseModel):
    user: User
    today_mood: Optional[Mood] = None
    daily_tip: Optional[WellnessTip] = None
    recent_journal_entries: List[JournalEntry] = []
    mood_trend: List[Mood] = []
