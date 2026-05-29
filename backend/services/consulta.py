import re
from datetime import datetime, date
from uuid import uuid4
from core.data import consultas, idosos, medicos
from core.errors import ValidationError, UnauthorizedError


def _validar_data(data_str: str):
    try:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def _validar_hora(hora: str) -> str | None:
    hora = (hora or "").strip()
    if re.match(r"^\d{2}:\d{2}:\d{2}$", hora):
        hora = hora[:5]
    if re.match(r"^\d{2}:\d{2}$", hora):
        return hora
    return None


def agendar_consulta(data: dict, user_id: str) -> dict:
    if not user_id:
        raise UnauthorizedError("NAO_AUTORIZADO", "Token inválido ou ausente")

    idoso_id = (data.get("idosoId") or "").strip()
    medico_id = (data.get("medicoId") or "").strip()
    data_str = (data.get("data") or "").strip()
    hora = (data.get("hora") or "").strip()
    local = (data.get("local") or "").strip()
    observacoes = (data.get("observacoes") or "").strip()

    if not idoso_id:
        raise ValidationError("IDOSO_OBRIGATORIO", "Idoso obrigatório")
    if not any(i["id"] == idoso_id for i in idosos):
        raise ValidationError("IDOSO_NAO_ENCONTRADO", "Idoso não encontrado")
    if not medico_id:
        raise ValidationError("MEDICO_OBRIGATORIO", "Médico obrigatório")
    if not any(m["id"] == medico_id for m in medicos):
        raise ValidationError("MEDICO_NAO_ENCONTRADO", "Médico não encontrado")
    if not data_str:
        raise ValidationError("DATA_OBRIGATORIA", "Data obrigatória")

    data_consulta = _validar_data(data_str)
    if not data_consulta or data_consulta < date.today():
        raise ValidationError("DATA_INVALIDA", "Data deve ser hoje ou no futuro")

    hora = _validar_hora(hora)
    if not hora:
        raise ValidationError("HORA_INVALIDA", "Hora inválida")
    if not local:
        raise ValidationError("LOCAL_OBRIGATORIO", "Local obrigatório")

    consulta = {
        "id": str(uuid4()),
        "idosoId": idoso_id,
        "medicoId": medico_id,
        "data": data_str,
        "hora": hora,
        "local": local,
        "observacoes": observacoes,
        "status": "agendada",
    }
    consultas.append(consulta)
    return consulta


def listar_consultas() -> list:
    return consultas
