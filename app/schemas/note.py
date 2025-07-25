from pydantic import BaseModel
from datetime import datetime

class NoteBase(BaseModel):
    timestamp_label: str
    note_text: str

class NoteCreate(NoteBase):
    video_id: str

class NoteUpdate(BaseModel):
    note_text: str

class NoteOut(NoteBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

NoteResponse = NoteOut
