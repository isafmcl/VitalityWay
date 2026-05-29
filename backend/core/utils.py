from flask import jsonify
from datetime import datetime


def ts() -> str:
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def erro(mensagem: str, codigo: str, status: int = 400):
    return jsonify({"status": "erro", "mensagem": mensagem, "codigoErro": codigo, "timestamp": ts()}), status


def sucesso(mensagem: str, dados=None, status: int = 201):
    body = {"status": "sucesso", "mensagem": mensagem}
    if dados is not None:
        body["dados"] = dados
    return jsonify(body), status
