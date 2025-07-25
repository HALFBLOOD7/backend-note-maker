from fastapi import APIRouter, Depends, HTTPException,  status
from sqlalchemy.orm import Session
from app.schemas.video import VideoCreate, VideoResponse
from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.crud.video import (
    create_video,
    get_videos_by_user,
    get_videos_by_user_bookmarked,
    toggle_videos_bookmark,
    delete_video,
    get_video_bookmark_status)

router = APIRouter(tags=["videos"])

@router.post("/", response_model=VideoResponse)
def create(video_data: VideoCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success = create_video(db, user.id, video_data)
    if(not success):
        raise HTTPException(
            status_code=400,
            detail="Video already exists for this user with the same platform and embed URL."
        )
    return success

@router.get("/", response_model=list[VideoResponse])
def list_videos(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_videos_by_user(db, user.id)

@router.get("/bookmark", response_model=list[VideoResponse])
def list_bookmarked_videos(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_videos_by_user_bookmarked(db, user.id)

@router.get("/isBookmarked/{video_id}", response_model=bool)
def is_video_bookmarked(video_id:str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_video_bookmark_status(db, user.id, video_id)

@router.post("/bookmark/{video_id}", status_code=status.HTTP_204_NO_CONTENT)
def list_toggle_bookmark_videos(video_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return toggle_videos_bookmark(db, user.id, video_id)

@router.delete("/{video_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_video(video_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success = delete_video(db, user.id, video_id)
    if not success:
        raise HTTPException(status_code=404, detail="Video not found or not authorized to delete")
    return