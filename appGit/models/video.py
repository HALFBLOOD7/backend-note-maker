import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=True)
    platform = Column(String, nullable=False)  # 'youtube' or 'vimeo'
    external_id = Column(String, nullable=True)
    embed_url = Column(String, nullable=False)
    thumbnail_url = Column(String, nullable=True)
    completed_count = Column(Integer, default=0)
    last_watched = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="videos")
    notes = relationship("Note", back_populates="video", cascade="all, delete-orphan")
    bookmarks = relationship("Bookmark", back_populates="video", cascade="all, delete-orphan")
    playlist_videos = relationship("PlaylistVideo", back_populates="video", cascade="all, delete-orphan")
