from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models.playlist import Playlist
from app.models.playlist_video import PlaylistVideo
from app.models.video import Video
from app.schemas.playlist import PlaylistCreate
import uuid


def create_playlist(db: Session, user_id: str, playlist: PlaylistCreate):
    db_playlist = Playlist(
        id=str(uuid.uuid4()),
        user_id=user_id,
        name=playlist.name
    )
    try:
        db.add(db_playlist)
        db.commit()
        db.refresh(db_playlist)
        return db_playlist
    except IntegrityError as e:
        db.rollback()
        raise ValueError(f'Playlist "{playlist.name}" already exists for this user.')

def add_video_to_playlist(db: Session, playlist_id: str, video_id: str):
    link = PlaylistVideo(
        id=str(uuid.uuid4()),
        playlist_id=playlist_id,
        video_id=video_id
    )
    db.add(link)
    db.commit()
    return link

def get_videos_by_playlist(db: Session, user_id: str, playlist_id: str):
    playlist = db.query(Playlist).filter_by(id = playlist_id,user_id = user_id).first()

    if not playlist:    
        return playlist 
    
    videos = (
        db.query(Video)
        .join(PlaylistVideo, PlaylistVideo.video_id == Video.id)
        .filter(PlaylistVideo.playlist_id == playlist_id)
        .all()
    )

    return videos
def get_videos_id_by_playlist(db: Session, user_id: str, playlist_id: str):
    playlist = db.query(Playlist).filter_by(id = playlist_id,user_id = user_id).first()

    if not playlist:    
        return playlist 
    links =db.query(PlaylistVideo.video_id).filter(PlaylistVideo.playlist_id == playlist_id).all()
    
    return [video_id for (video_id,) in links]

def remove_video_from_playlist(db: Session, playlist_id: str, video_id: str):
    link = db.query(PlaylistVideo).filter_by(playlist_id=playlist_id, video_id=video_id).first()
    if link:
        db.delete(link)
        db.commit()

def get_playlists_by_user(db: Session, user_id: str):
    return db.query(Playlist).filter_by(user_id=user_id).all()

def get_playlist_detail(db:Session, user_id: str, playlist_id: str):
    return db.query(Playlist).filter_by(id=playlist_id,user_id=user_id).first()

def delete_playlist_by_user(db: Session,user_id: str, playlist_id: str):
    playlist = db.query(Playlist).filter_by(id = playlist_id,user_id = user_id).first()
    if not playlist:
        return False
    links = db.query(PlaylistVideo).filter_by(playlist_id=playlist_id).all()
    for link in links:
        db.delete(link)
    db.delete(playlist)
    db.commit()
    return True
