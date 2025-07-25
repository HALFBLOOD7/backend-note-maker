from sqlalchemy.orm import Session
from app.models.bookmark import Bookmark
from app.schemas.bookmark import BookmarkCreate
import uuid

def create_bookmark(db: Session, user_id: str, bookmark: BookmarkCreate):
    db_bookmark = Bookmark(
        id=str(uuid.uuid4()),
        user_id=user_id,
        video_id=bookmark.video_id,
        timestamp_seconds=bookmark.timestamp_seconds,
        label=bookmark.label
    )
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark

def get_bookmarks_by_video(db: Session, user_id: str, video_id: str):
    return db.query(Bookmark).filter_by(user_id=user_id, video_id=video_id).all()

def delete_bookmark(db: Session, bookmark: Bookmark):
    db.delete(bookmark)
    db.commit()
