from pathlib import Path
from fastapi import FastAPI, Request
from app.sessions import sessions


def get_query(name: str) -> str:
    base = Path(__file__).resolve().parents[0]
    queries_dir = base / "queries"
    path = queries_dir / name
    return path.read_text()


def is_logged_in(request: Request) -> bool:
    session_token = request.cookies.get("username_session_token")
    username = sessions.get(session_token)
    return username != None
    

def get_username(request: Request) -> str:
    session_token = request.cookies.get("username_session_token")
    username = sessions.get(session_token)
    return username
