from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse
from app.core.dependencies import get_db, get_current_user
from app.crud.bookmark import create_bookmark, get_bookmarks_by_video
from app.models.user import User

router = APIRouter( tags=["bookmarks"])

@router.post("/", response_model=BookmarkResponse)
def add(bookmark: BookmarkCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_bookmark(db, bookmark, user.id)

@router.get("/{video_id}", response_model=list[BookmarkResponse])
def list_bookmarks(video_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_bookmarks_by_video(db, video_id, user.id)
