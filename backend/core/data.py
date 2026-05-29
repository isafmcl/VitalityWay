from datetime import datetime

usuarios = [
    {"id": "u1", "email": "cuidador@email.com", "senha": "12345678", "nome": "Ana Cuidadora", "perfil": "cuidador"},
    {"id": "u2", "email": "admin@email.com",    "senha": "admin123",  "nome": "Admin",         "perfil": "admin"},
]

especialidades = [
    {"id": "e1", "nome": "Cardiologia"},
    {"id": "e2", "nome": "Geriatria"},
    {"id": "e3", "nome": "Neurologia"},
]

medicos = [
    {"id": "m1", "nome": "Dra. Ana Lima",    "crm": "123456", "especialidadeId": "e1"},
    {"id": "m2", "nome": "Dr. Carlos Melo",  "crm": "654321", "especialidadeId": "e2"},
]

idosos = [
    {"id": "i1", "nome": "Maria Aparecida", "dataNascimento": "1945-03-12"},
    {"id": "i2", "nome": "José Ferreira",   "dataNascimento": "1938-07-20"},
]

consultas = []

tokens_validos = {}  # token -> usuario_id
