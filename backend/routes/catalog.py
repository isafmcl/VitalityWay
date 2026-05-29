from flask import Blueprint
from core.utils import erro, sucesso
from core.errors import AppError
from services.catalog import listar_especialidades, listar_idosos

bp = Blueprint("catalog", __name__)


@bp.route("/especialidades", methods=["GET"])
def obter_especialidades():
    try:
        return sucesso("Especialidades listadas com sucesso", listar_especialidades(), 200)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/idosos", methods=["GET"])
def obter_idosos():
    try:
        return sucesso("Idosos listados com sucesso", listar_idosos(), 200)
    except AppError as exc:
        return erro(exc.mensagem, exc.codigo, exc.status)


@bp.route("/health", methods=["GET"])
def health():
    return sucesso("API ativa", {"status": "ok"}, 200)
