from models.usuario_model import listar

def listar_todos():
    usuarios = listar()
    return usuarios