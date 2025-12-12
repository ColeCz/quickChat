from fastapi import FastAPI, APIRouter, Response, Request, Cookie
from app.helpers import get_query, is_logged_in, get_username
from app.database import pool
from app.sessions import sessions
from app.routes.users import verify_user_exists
import secrets

router = APIRouter()

# TODO: check if friends are friends before sending friend request

@router.post("/send-friend-request")
def send_friend_request(request: Request, receiver_username: str = None):

    if not is_logged_in(request):
        return {"error:": "Must be logged in to perform this operation"}

    if receiver_username == None:
        return {"error:": "No username given"}

    if not verify_user_exists(receiver_username):
        return {"error:": "The user you are sending a friend request to does not exist"}

    sender_username = get_username(request)
    sql = get_query("send-friend-request.sql")
    parameters = {
        "sender_username": sender_username,
        "receiver_username": receiver_username
    }

    try:
        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
                return {"success:": "friend request sent"}
    except Exception as e:
        return {"error:": str(e)}


@router.post("/accept-friend-request")
def accept_friend_request(request: Request, sender_username: str):

    if not is_logged_in(request):
        return {"error:": "must be logged in to perform this operation"}

    if not sender_username:
        return {"error:": "frontend must share the username of the friend were accepting"}

    username = get_username(request)
    sql = get_query("accept-friend-request.sql")

    parameters = {
        "receiver_username": username,
        "sender_username": sender_username
    }

    try:
        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
    except Exception as e:
        return {"error:": str(e)}

    return {"success:": "friendship status updated"}

    
@router.get("/get-friends-list")
def get_friends_list(request: Request):
    
    if not is_logged_in(request):
        return {"error:": "must be logged in to perform this operation"}

    username = get_username(request)
    parameters = {"username": username}
    sql = get_query("get-friends.sql")

    try:
        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
                output = cursor.fetchall()
    except Exception as e:
        return {"error:": str(e)}

    sorted_output = sorted(output)

    return sorted_output


@router.get("/get-friend-requests")
def get_friend_requests(request: Request):

    if not is_logged_in(request):
        return {"error:": "must be logged in to perform this operation"}

    username = get_username(request)
    sql = get_query("get-incoming-requests.sql")
    parameters = {"username": username}

    try:
        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parameters)
                output = cursor.fetchall()
    except Exception as e:
        return {"error:": str(e)}

    return output
