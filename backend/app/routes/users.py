from fastapi import FastAPI, APIRouter, Response, Request, Cookie
from app.helpers import get_query, is_logged_in, get_username
from app.database import pool
from app.sessions import sessions
import secrets

# TODO: logout before logging in
# TODO: Remove cookie/session logic from login and add to helper function
# TODO: use the login helper function to automatically sign users in upon registration


router = APIRouter()

def verify_user_exists(username: str) -> bool:

    if username == None:
        return False

    sql = get_query("verify-user-exists.sql")
    parameters = {
        "username": username
    }

    try:
        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
                row = cursor.fetchone()
    except Exception as e:
        return {"error:": str(e)}

    if row:
        return row[0] == 1
    else:
        return False

    

@router.post("/login")
def login(response: Response, username: str = None, password: str = None):
    if username == None:
        return {"error:": "missing username"}
    elif password == None:
        return {"error:" "missing password"}

    sql = get_query("authenticate-user.sql")
    parameters = {
        "username": username,
        "passwrd": password
    }

    try:
        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
                row = cursor.fetchone()
    except Exception as e:
        return {"error:": str(e)}

    if row:
        # set session
        fetched_username = row[0]
        session_token = secrets.token_hex(32)
        sessions[session_token] = username

        # set cookie
        response.set_cookie(
            key="username_session_token",
            value=session_token,
            httponly=True,   # JS cannot read it
            secure=False,    # NOTE: true if using HTTPS
            samesite="lax"
        )

    else:
        return {"error": "invalid credentials"}

    return_string = "User logged in: username=" + fetched_username
    return {"Success": return_string}



@router.post("/logout")
def logout(response: Response, username_session_token: str = Cookie(None)):
    removed_session_val = sessions.pop(username_session_token, None)
    response.delete_cookie("username_session_token")
    return {"Success - removed the session value:": removed_session_val}
    


@router.post("/register")
def register(username: str = None, password: str = None):
    if username == None:
        return {"error:": "missing username"}
    elif password == None:
        return {"error:" "missing password"}

    sql = get_query("register-user.sql")
    parameters = {
        "username": username,
        "passwrd": password
    }

    try:
        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
    except Exception as e:
        return {"error:": str(e)}

    return {"success": "account created"}
