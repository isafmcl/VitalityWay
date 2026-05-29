from flask import Blueprint, request
from core.auth import get_authorized_user
from core.utils import erro, sucesso
from core.errors import AppError
from services.medico import cadastrar_medico, listar_medicos

bp = Blueprint("medico", __name__)


@bp.route("/medicos", methods=["POST"])
def criar_medico():
    user_id = get_authorized_user(request)
    data = request.get_json(silent=True)
    if data is None:
        data = request.form.to_dict() or {}
    try:
        novo_medico = cadastrar_medico(data, user_id)
        return sucesso("Médico cadastrado com sucesso", novo_medico, 201)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/medicos", methods=["GET"])
def obter_medicos():
    return sucesso("Médicos listados com sucesso", listar_medicos(), 200)
