from pydantic import BaseModel
from typing import List
from datetime import datetime

class PlaylistBase(BaseModel):
    name: str

class PlaylistCreate(PlaylistBase):
    pass

class PlaylistResponse(PlaylistBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True

class PlaylistVideoSchema(BaseModel):
    id: str
    video_id: str
    playlist_id: str
    added_at: datetime

    class Config:
        orm_mode = True

class PlaylistDetailSchema(BaseModel):
    id: str
    name: str
    created_at: datetime
    playlist_videos: List[PlaylistVideoSchema] = []

    class Config:
        orm_mode = True
