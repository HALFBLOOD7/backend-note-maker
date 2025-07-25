from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate
import uuid

def create_note(db: Session, user_id: str, note: NoteCreate):
    db_note = Note(
        id=str(uuid.uuid4()),
        user_id=user_id,
        video_id=note.video_id,
        timestamp_label=note.timestamp_label,
        note_text=note.note_text
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes_by_video(db: Session, user_id: str, video_id: str):
    return db.query(Note).filter_by(user_id=user_id, video_id=video_id).all()

def update_note(db: Session, user_id: str, note_id: str, note_data: NoteUpdate):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()
    if not note:
        return None

    note.note_text = note_data.note_text
    db.commit()
    db.refresh(note)
    return note


def delete_note_by_id(db: Session, user_id: str, note_id: str):
    note = db.query(Note).filter_by(id=note_id, user_id=user_id).first()
    if note:
        db.delete(note)
        db.commit()
        return True
    return False
