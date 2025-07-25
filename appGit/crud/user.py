from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from app.crud.settings import create_or_update_settings
from app.schemas.settings import SettingsCreate

import uuid

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = User(
        id=str(uuid.uuid4()),
        email=user.email,
        password_hash=hashed_pw,
        name=user.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    default_settings = SettingsCreate(
        theme="light",
        playback_speed=1.0,
        autosave_notes=True
    )
    create_or_update_settings(db, db_user.id, default_settings)
    return db_user
