from sqlalchemy.orm import Session
from app.models.video import Video
from app.models.playlist import Playlist
from app.models.bookmark import Bookmark
from app.schemas.video import VideoCreate
import uuid

def create_video(db: Session, user_id: str, video: VideoCreate):
    # Check for existing video with the same user_id, platform, and embed_url
    existing_video = db.query(Video).filter_by(
        user_id=user_id,
        platform=video.platform,
        embed_url=video.embed_url
    ).first()

    if existing_video:
        return False

    # Create new video
    db_video = Video(
        id=str(uuid.uuid4()),
        user_id=user_id,
        title=video.title,
        platform=video.platform,
        external_id=video.external_id,
        embed_url=video.embed_url,
        thumbnail_url=video.thumbnail_url,
    )
    
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


def get_videos_by_user(db: Session, user_id: str):
    return db.query(Video).filter(Video.user_id == user_id).all()

def get_video_by_id(db: Session, video_id: str):
    return db.query(Video).filter(Video.id == video_id).first()

def get_videos_by_playlist(db: Session, playlist_id: str, user_id: str):
    playlist = db.query(Playlist).filter(Playlist.id == playlist_id, Playlist.user_id == user_id).first()
    if not playlist:
        return None
    return playlist.videos  


def delete_video(db: Session, user_id: str, video_id: str) -> bool:
    video = db.query(Video).filter(Video.id == video_id, Video.user_id == user_id).first()
    if not video:
        return False
    db.delete(video)
    db.commit()
    return True

def increment_video_completion(db: Session, video: Video):
    video.completed_count += 1
    db.commit()
    db.refresh(video)
    return video

def get_videos_by_user_bookmarked(db: Session, user_id: str):
    return (
        db.query(Video)
        .join(Bookmark)
        .filter(Bookmark.user_id == user_id)
        .all()
    )

def toggle_videos_bookmark(db: Session, user_id: str, video_id: str):
    bookmark = (
        db.query(Bookmark)
        .filter(Bookmark.user_id == user_id, Bookmark.video_id == video_id)
        .first()
    )
    

    if bookmark:
        db.delete(bookmark)
    else:
        new_bookmark = Bookmark(user_id=user_id, video_id=video_id)
        db.add(new_bookmark)

    db.commit()

def get_video_bookmark_status(db: Session, user_id: str, video_id: str):
    bookmark = (
        db.query(Bookmark)
        .filter(Bookmark.user_id == user_id, Bookmark.video_id == video_id)
        .first()
    )

    if bookmark:
        return True
    return False

