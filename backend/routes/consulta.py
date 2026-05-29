from flask import Blueprint, request
from core.auth import get_authorized_user
from core.utils import erro, sucesso
from core.errors import AppError
from services.consulta import agendar_consulta, listar_consultas

bp = Blueprint("consulta", __name__)


@bp.route("/consultas", methods=["POST"])
def criar_consulta():
    user_id = get_authorized_user(request)
    data = request.get_json(silent=True)
    if data is None:
        data = request.form.to_dict() or {}
    try:
        consulta = agendar_consulta(data, user_id)
        return sucesso("Consulta agendada com sucesso", consulta, 201)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/consultas", methods=["GET"])
def obter_consultas():
    return sucesso("Consultas listadas com sucesso", listar_consultas(), 200)
