from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.note import NoteCreate, NoteResponse, NoteUpdate
from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from fastapi import HTTPException, status
from app.crud.note import (
    create_note,
    get_notes_by_video,
    delete_note_by_id,
    update_note
    )

router = APIRouter(tags=["notes"])

@router.post("/", response_model=NoteResponse)
def add_note(note: NoteCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_note(db, user.id, note)

@router.get("/{video_id}", response_model=list[NoteResponse])
def get_notes(video_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_notes_by_video(db, user.id, video_id)

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    success = delete_note_by_id(db, user.id, note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return status.HTTP_200_OK

@router.put("/{note_id}", response_model=NoteResponse)
def edit_note(
    note_id: str,
    note_update: NoteUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    updated_note = update_note(db, user.id, note_id, note_update)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note
