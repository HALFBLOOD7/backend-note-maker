from sqlalchemy.orm import Session
from app.models.settings import Settings
from app.schemas.settings import SettingsCreate
import uuid

def get_settings_by_user(db: Session, user_id: str):
    return db.query(Settings).filter_by(user_id=user_id).first()

def create_or_update_settings(db: Session, user_id: str, settings_data: SettingsCreate):
    settings = get_settings_by_user(db, user_id)
    if settings:
        settings.theme = settings_data.theme
        settings.playback_speed = settings_data.playback_speed
        settings.autosave_notes = settings_data.autosave_notes
    else:
        settings = Settings(
            id=str(uuid.uuid4()),
            user_id=user_id,
            theme=settings_data.theme,
            playback_speed=settings_data.playback_speed,
            autosave_notes=settings_data.autosave_notes
        )
        db.add(settings)
    db.commit()
    db.refresh(settings)
    return settings
