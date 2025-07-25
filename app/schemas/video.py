from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VideoBase(BaseModel):
    title: Optional[str]
    platform: str
    external_id: Optional[str]
    embed_url: str
    thumbnail_url: Optional[str]

class VideoCreate(VideoBase):
    pass

class VideoOut(VideoBase):
    id: str
    completed_count: int
    last_watched: Optional[datetime]
    created_at: datetime

    class Config:
        orm_mode = True

VideoResponse = VideoOut 
