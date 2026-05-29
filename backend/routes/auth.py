from flask import Blueprint, request
from core.auth import get_authorized_user
from core.data import usuarios
from core.utils import erro, sucesso
from services.auth import login as action_login, signup as action_signup
from core.errors import AppError

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["POST"])
def login():
    # Accept JSON or form-encoded bodies (URLSearchParams)
    data = request.get_json(silent=True)
    if data is None:
        data = request.form.to_dict() or {}
    try:
        result = action_login(data)
        return sucesso("Login realizado com sucesso", result, 200)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/session", methods=["GET"])
def session():
    user_id = get_authorized_user(request)
    if not user_id:
        return erro("Token inválido ou expirado", "NAO_AUTORIZADO", 401)
    usuario = next((u for u in usuarios if u["id"] == user_id), None)
    if not usuario:
        return erro("Usuário não encontrado", "USUARIO_NAO_ENCONTRADO", 404)
    return sucesso(
        "Sessão válida",
        {"usuario": {"id": usuario["id"], "nome": usuario["nome"], "perfil": usuario["perfil"]}},
        200,
    )


@bp.route("/signup", methods=["POST"])
def signup():
    # Accept JSON or form-encoded bodies (URLSearchParams)
    data = request.get_json(silent=True)
    if data is None:
        data = request.form.to_dict() or {}
    try:
        result = action_signup(data)
        return sucesso("Usuário cadastrado com sucesso", result, 201)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)
