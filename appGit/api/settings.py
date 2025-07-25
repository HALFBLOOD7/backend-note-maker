from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.settings import SettingsCreate, SettingsResponse
from app.core.dependencies import get_db, get_current_user
from app.crud.settings import create_or_update_settings, get_settings_by_user
from app.models.user import User

router = APIRouter( tags=["settings"])

@router.post("/", response_model=SettingsResponse)
def upsert(settings: SettingsCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_or_update_settings(db, user.id, settings)

@router.get("/", response_model=SettingsResponse)
def get(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_settings_by_user(db, user.id)
