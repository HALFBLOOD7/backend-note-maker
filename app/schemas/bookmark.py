from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BookmarkBase(BaseModel):
    user_id: str
    video_id: str

class BookmarkCreate(BookmarkBase):
    pass

class BookmarkResponse(BookmarkBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
