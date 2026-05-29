from .auth import login
from .medico import cadastrar_medico, listar_medicos
from .consulta import agendar_consulta, listar_consultas
from .catalog import listar_especialidades, listar_idosos

__all__ = [
    "login",
    "cadastrar_medico",
    "listar_medicos",
    "agendar_consulta",
    "listar_consultas",
    "listar_especialidades",
    "listar_idosos",
]
