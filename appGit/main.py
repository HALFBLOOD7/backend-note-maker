from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import (
    auth,
    users,
    videos,
    notes,
    bookmarks,
    playlists,
    settings,
)

app = FastAPI(title="Video Note Maker Backend")

# Register all routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(videos.router, prefix="/videos", tags=["videos"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(bookmarks.router, prefix="/bookmarks", tags=["bookmarks"])
app.include_router(playlists.router, prefix="/playlists", tags=["playlists"])
app.include_router(settings.router, prefix="/settings", tags=["settings"])

# CORS setup (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Video Note Maker Backend!"}

