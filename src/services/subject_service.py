#conversa com o banco, aplica regras e usa as classes

import sqlite3
from models.subject import Materia

class SubjectService:
    def criar_materia(self, nome):
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO materias (nome) VALUES (?)", nome)
        conexao.commit()

        materia_id = cursor.lastrowid #duvida
        conexao.close()
        return Materia(nome = nome, id = materia_id)
    
    def listar_materias(self):
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome FROM materias")
        linhas = cursor.fetchall() #duvida - devolve todas as linhas

        conexao.close()
        materias = []

        for linha in linhas:
            materia = Materia(id = linha[0], nome = linha[1])
            materias.append(materia)

            return materias
        
    def excluir_materia(self, materia_id):
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM materias WHERE id = ?", (materia_id))

        conexao.commit
        conexao.close
    
    
