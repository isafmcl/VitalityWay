import re
from uuid import uuid4
from core.data import usuarios, tokens_validos
from core.errors import ValidationError, UnauthorizedError, ConflictError


def _validar_email(email: str) -> bool:
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))


def login(data: dict) -> dict:
    email = (data.get("email") or "").strip()
    senha = (data.get("senha") or "").strip()

    if not email:
        raise ValidationError("EMAIL_OBRIGATORIO", "E-mail obrigatório")
    if not _validar_email(email):
        raise ValidationError("EMAIL_INVALIDO", "E-mail inválido")
    if not senha:
        raise ValidationError("SENHA_OBRIGATORIA", "Senha obrigatória")

    usuario = next((u for u in usuarios if u["email"] == email), None)
    if not usuario or usuario["senha"] != senha:
        raise UnauthorizedError("CREDENCIAIS_INVALIDAS", "Credenciais inválidas")

    token = str(uuid4())
    tokens_validos[token] = usuario["id"]

    return {
        "token": token,
        "usuario": {"id": usuario["id"], "nome": usuario["nome"], "perfil": usuario["perfil"]},
    }


def signup(data: dict) -> dict:
    email = (data.get("email") or "").strip()
    senha = (data.get("senha") or "").strip()
    nome = (data.get("nome") or "").strip()

    if not email:
        raise ValidationError("EMAIL_OBRIGATORIO", "E-mail obrigatório")
    if not _validar_email(email):
        raise ValidationError("EMAIL_INVALIDO", "E-mail inválido")
    if not senha:
        raise ValidationError("SENHA_OBRIGATORIA", "Senha obrigatória")
    if len(senha) < 6:
        raise ValidationError("SENHA_MUITO_CURTA", "Senha deve ter pelo menos 6 caracteres")
    if not nome:
        raise ValidationError("NOME_OBRIGATORIO", "Nome obrigatório")

    # Check if email already exists
    if any(u["email"] == email for u in usuarios):
        raise ConflictError("EMAIL_JA_EXISTE", "E-mail já cadastrado")

    # Create new user
    novo_usuario = {
        "id": str(uuid4()),
        "email": email,
        "senha": senha,
        "nome": nome,
        "perfil": "cuidador",
    }
    usuarios.append(novo_usuario)

    return {
        "id": novo_usuario["id"],
        "email": novo_usuario["email"],
        "nome": novo_usuario["nome"],
        "perfil": novo_usuario["perfil"],
    }
