from pydantic import BaseModel
# from datetime import datetime

class SettingsBase(BaseModel):
    theme: str = "light"
    playback_speed: float = 1.0
    autosave_notes: bool = True

class SettingsCreate(SettingsBase):
    pass

class SettingsResponse(SettingsBase):
    id: str
    # created_at: datetime
    # updated_at: datetime

    class Config:
        orm_mode = True
