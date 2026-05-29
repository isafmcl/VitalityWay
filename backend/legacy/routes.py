from flask import Blueprint, request
from auth import get_authorized_user
from errors import AppError
from services import (
    login as action_login,
    cadastrar_medico,
    listar_medicos,
    listar_consultas,
    listar_especialidades,
    listar_idosos,
    agendar_consulta,
)
from utils import erro, sucesso

bp = Blueprint("api", __name__)


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    try:
        result = action_login(data)
        return sucesso("Login realizado com sucesso", result, 200)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/medicos", methods=["POST"])
def criar_medico():
    user_id = get_authorized_user(request)
    data = request.get_json(silent=True) or {}
    try:
        novo_medico = cadastrar_medico(data, user_id)
        return sucesso("Médico cadastrado com sucesso", novo_medico, 201)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/medicos", methods=["GET"])
def obter_medicos():
    return sucesso("Médicos listados com sucesso", listar_medicos(), 200)


@bp.route("/consultas", methods=["POST"])
def criar_consulta():
    user_id = get_authorized_user(request)
    data = request.get_json(silent=True) or {}
    try:
        consulta = agendar_consulta(data, user_id)
        return sucesso("Consulta agendada com sucesso", consulta, 201)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/consultas", methods=["GET"])
def obter_consultas():
    return sucesso("Consultas listadas com sucesso", listar_consultas(), 200)


@bp.route("/especialidades", methods=["GET"])
def obter_especialidades():
    return sucesso("Especialidades listadas com sucesso", listar_especialidades(), 200)


@bp.route("/idosos", methods=["GET"])
def obter_idosos():
    return sucesso("Idosos listados com sucesso", listar_idosos(), 200)


@bp.route("/health", methods=["GET"])
def health():
    return sucesso("API ativa", {"status": "ok"}, 200)


def register_routes(app):
    app.register_blueprint(bp)
