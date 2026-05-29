from flask import request
from core.data import tokens_validos


def get_token(req: request):
    auth = req.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        return auth[7:]
    # Fallback: allow token via query string to avoid CORS preflight issues
    token_qs = req.args.get("token")
    if token_qs:
        return token_qs
    return None


def get_authorized_user(req: request):
    token = get_token(req)
    return tokens_validos.get(token)
