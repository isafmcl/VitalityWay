import re
from uuid import uuid4
from core.data import medicos, especialidades
from core.errors import ValidationError, ConflictError, UnauthorizedError


def _validar_crm(crm: str) -> bool:
    return bool(re.match(r"^\d{6,7}$", crm))


def cadastrar_medico(data: dict, user_id: str) -> dict:
    if not user_id:
        raise UnauthorizedError("NAO_AUTORIZADO", "Token inválido ou ausente")

    nome = (data.get("nome") or "").strip()
    crm = (data.get("crm") or "").strip()
    especialidade_id = (data.get("especialidadeId") or "").strip()

    if not nome:
        raise ValidationError("NOME_OBRIGATORIO", "Nome obrigatório")
    if not _validar_crm(crm):
        raise ValidationError("CRM_INVALIDO", "CRM inválido")
    if not especialidade_id:
        raise ValidationError("ESPECIALIDADE_OBRATORIA", "Especialidade obrigatória")
    if not any(e["id"] == especialidade_id for e in especialidades):
        raise ValidationError("ESPECIALIDADE_NAO_ENCONTRADA", "Especialidade não encontrada")
    if any(m["crm"] == crm for m in medicos):
        raise ConflictError("CRM_DUPLICADO", "CRM já cadastrado")

    novo_medico = {"id": str(uuid4()), "nome": nome, "crm": crm, "especialidadeId": especialidade_id}
    medicos.append(novo_medico)
    return novo_medico


def listar_medicos() -> list:
    return medicos
