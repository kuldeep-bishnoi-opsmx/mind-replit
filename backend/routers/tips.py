from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from datetime import datetime

from database import get_db
from models import User, WellnessTip as WellnessTipModel, UserTipView
from schemas import WellnessTip
from services.auth_service import get_current_user

router = APIRouter()

@router.get("/daily", response_model=WellnessTip)
async def get_daily_tip(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a random wellness tip that the user hasn't seen recently."""
    
    viewed_tip_ids = db.query(UserTipView.tip_id).filter(
        UserTipView.user_id == current_user.id
    ).subquery()
    
    tip = db.query(WellnessTipModel).filter(
        WellnessTipModel.is_active == True,
        ~WellnessTipModel.id.in_(viewed_tip_ids)
    ).order_by(func.random()).first()
    
    if not tip:
        tip = db.query(WellnessTipModel).filter(
            WellnessTipModel.is_active == True
        ).order_by(func.random()).first()
    
    if not tip:
        raise HTTPException(status_code=404, detail="No wellness tips available")
    
    view = UserTipView(user_id=current_user.id, tip_id=tip.id)
    db.add(view)
    db.commit()
    
    return tip

@router.get("/", response_model=List[WellnessTip])
async def get_all_tips(
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get all wellness tips, optionally filtered by category."""
    query = db.query(WellnessTipModel).filter(WellnessTipModel.is_active == True)
    
    if category:
        query = query.filter(WellnessTipModel.category == category)
    
    tips = query.all()
    
    return tips
