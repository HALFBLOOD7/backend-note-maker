from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.playlist import PlaylistCreate, PlaylistResponse, PlaylistDetailSchema
from app.schemas.video import VideoResponse
from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.crud.playlist import (
    create_playlist,
    get_playlist_detail,
    get_playlists_by_user,
    delete_playlist_by_user,
    get_videos_by_playlist,
    get_videos_id_by_playlist,
    add_video_to_playlist,
    remove_video_from_playlist
)
router = APIRouter( tags=["playlists"])

@router.post("/", response_model=PlaylistResponse)
def create(
    playlist: PlaylistCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    try:
        return create_playlist(db, user.id, playlist)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{playlist_id}/videos/{video_id}", status_code=status.HTTP_201_CREATED)
def add_video(playlist_id: str, video_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success = add_video_to_playlist(db, playlist_id, video_id)
    if not success:
        raise HTTPException(status_code=404, detail="Playlist not found or not authorized")
    return 

@router.get("/", response_model=list[PlaylistResponse])
def list_playlists(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_playlists_by_user(db, user.id)

@router.get("/{playlist_id}/videos", response_model=list[VideoResponse])
def list_videos_id_by_playlist(
    playlist_id: str, 
    db: Session = Depends(get_db), 
    user: User = Depends(get_current_user)
):
    videos = get_videos_by_playlist(db, user.id, playlist_id)
    if videos is None:
        raise HTTPException(status_code=404, detail="Playlist not found or not authorized")
    return videos

@router.get("/{playlist_id}/videosId", response_model=list[str])
def list_videos_id_by_playlist(
    playlist_id: str, 
    db: Session = Depends(get_db), 
    user: User = Depends(get_current_user)
):
    videos = get_videos_id_by_playlist(db, user.id, playlist_id)
    if videos is None:
        raise HTTPException(status_code=404, detail="Playlist not found or not authorized")
    return videos

@router.get("/{playlist_id}/detail",response_model=PlaylistDetailSchema)
def get_detail(
    playlist_id: str, 
    db: Session = Depends(get_db), 
    user: User = Depends(get_current_user)
):
    detail = get_playlist_detail(db,user.id,playlist_id)
    if detail is None:
        raise HTTPException(status_code=404, detail="Playlist not found or not authorized")
    return detail

@router.delete("/{playlist_id}/videos/{video_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_video(playlist_id: str, video_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success = remove_video_from_playlist(db, playlist_id, video_id)
    if not success:
        raise HTTPException(status_code=404, detail="Playlist not found or not authorized")

    return

@router.delete("/{playlist_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user_playlist(playlist_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success = delete_playlist_by_user(db, user.id, playlist_id)
    if not success:
        raise HTTPException(status_code=404, detail="Video not found or not authorized to delete")
    return