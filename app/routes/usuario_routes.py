from flask import Blueprint, jsonify
from app.controllers.usuario_controller import listar_todos

usuario_bp  = Blueprint("usuario", __name__, url_prefix="/usuario")

@usuario_bp.route("/", methods=["GET"])
def listar_usuarios():
    try:
        usuarios = listar_usuarios()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"message":e}), 500