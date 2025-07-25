# 🎥 FastAPI Video Bookmarking & Note-Taking API

A full-featured FastAPI backend for managing videos, bookmarks, notes, playlists, and user settings with JWT-based authentication. Built using FastAPI, SQLAlchemy, SQLite, and OAuth2.

**Base URL:** `https://backend-note-maker.onrender.com`

## 📦 Features

- 🔐 **JWT Auth** (Signup/Login)
- 🎬 **Videos** (Add, Delete, Bookmark, Check Bookmark Status)
- 📌 **Bookmarks** (Per video per user)
- 📝 **Notes** (CRUD on video-specific notes)
- 🎵 **Playlists** (Create, Add/Remove videos, List)
- ⚙️ **User Settings** (Create, Update, Retrieve)
- 👤 **User Info** (`/users/me`)
- ✅ Protected routes via OAuth2 & Bearer Tokens


## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
````

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

---

## 🔐 Authentication

Uses OAuth2 with Password Flow and JWT tokens.

* **Signup**: `POST /auth/signup`
* **Login**: `POST /auth/token`

  * Form fields: `username`, `password`
* All other endpoints require `Authorization: Bearer <token>` header

---

## 🗂️ API Modules

| Module         | Path Prefix  | Description                    |
| -------------- | ------------ | ------------------------------ |
| `auth.py`      | `/auth`      | User registration and login    |
| `users.py`     | `/users`     | Get current authenticated user |
| `videos.py`    | `/videos`    | Add, list, bookmark videos     |
| `bookmarks.py` | `/bookmarks` | Add/list bookmarks by video    |
| `notes.py`     | `/notes`     | CRUD notes for videos          |
| `playlists.py` | `/playlists` | Manage playlists and videos    |
| `settings.py`  | `/settings`  | Manage user-specific settings  |

---

## 📄 Example Requests

### Signup

```json
POST /auth/signup
{
  "email": "user@example.com",
  "password": "strongpassword"
}
```

### Login

```x-www-form-urlencoded
POST /auth/token
username=user@example.com
password=strongpassword
```

### Add Video

```json
POST /videos
{
  "platform": "YouTube",
  "embed_url": "https://youtube.com/embed/xyz",
  "title": "Example Video"
}
```

## 🛠️ Project Structure

```
app/
├── api/                # All routers (auth, videos, notes, etc.)
├── core/               # Auth, security, dependencies
├── crud/               # Business logic
├── models/             # SQLAlchemy models
├── schemas/            # Pydantic schemas
├── database.py         # DB session
└── main.py             # FastAPI app entry point
```

## 🗃️ Database

* SQLite by default (`sqlite:///./app.db`)
* SQLAlchemy ORM
* Models defined in `app/models/`


## 🔒 Security

* Passwords hashed with bcrypt (`passlib`)
* JWT tokens signed with HS256
* Token expiration configurable (default: 60 min)


## 📬 Contributing

1. Fork this repo
2. Create your feature branch: `git checkout -b feat/feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feat/feature-name`
5. Open a pull request


## 📃 License

MIT License — free for personal and commercial use.


## 🤝 Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [PassLib](https://passlib.readthedocs.io/)
* [PyJWT](https://pyjwt.readthedocs.io/)
