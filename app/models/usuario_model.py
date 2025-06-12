from app.services.db import conectar

def listar():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * from USUARIOS")
    usuarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    return usuarios