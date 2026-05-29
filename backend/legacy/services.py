import re
from datetime import datetime, date
from uuid import uuid4
from data import usuarios, medicos, especialidades, idosos, consultas, tokens_validos
from errors import ValidationError, UnauthorizedError, ConflictError


def _validar_email(email):
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


def _validar_crm(crm):
    return bool(re.match(r"^\d{6,7}$", crm))


def _validar_data(data_str):
    try:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def _validar_hora(hora):
    return bool(re.match(r"^\d{2}:\d{2}$", hora))


def login(data):
    email = (data.get("email") or "").strip()
    senha = (data.get("senha") or "").strip()

    if not email:
        raise ValidationError("EMAIL_OBRIGATORIO", "E-mail obrigatório")
    if not _validar_email(email):
        raise ValidationError("EMAIL_INVALIDO", "E-mail inválido")
    if not senha:
        raise ValidationError("SENHA_OBRATORIA", "Senha obrigatória")

    usuario = next((u for u in usuarios if u["email"] == email), None)
    if not usuario or usuario["senha"] != senha:
        raise UnauthorizedError("CREDENCIAIS_INVALIDAS", "Credenciais inválidas")

    token = str(uuid4())
    tokens_validos[token] = usuario["id"]

    return {
        "token": token,
        "usuario": {"id": usuario["id"], "nome": usuario["nome"], "perfil": usuario["perfil"]},
    }


def cadastrar_medico(data, user_id):
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
        raise ValidationError("ESPECIALIDADE_OBRIGATORIA", "Especialidade obrigatória")
    if not any(e["id"] == especialidade_id for e in especialidades):
        raise ValidationError("ESPECIALIDADE_NAO_ENCONTRADA", "Especialidade não encontrada")
    if any(m["crm"] == crm for m in medicos):
        raise ConflictError("CRM_DUPLICADO", "CRM já cadastrado")

    novo = {"id": str(uuid4()), "nome": nome, "crm": crm, "especialidadeId": especialidade_id}
    medicos.append(novo)
    return novo


def agendar_consulta(data, user_id):
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
    if not data_consulta or data_consulta <= date.today():
        raise ValidationError("DATA_INVALIDA", "Data inválida")
    if not _validar_hora(hora):
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


def listar_medicos():
    return medicos


def listar_consultas():
    return consultas


def listar_especialidades():
    return especialidades


def listar_idosos():
    return idosos
