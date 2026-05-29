from flask import request
from data import tokens_validos


def get_token(req):
    auth = req.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        return auth[7:]
    return None


def get_authorized_user(req):
    token = get_token(req)
    return tokens_validos.get(token)
