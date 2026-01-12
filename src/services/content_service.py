import sqlite3
from models.content import Conteudo

class ContentService:
    def listar_por_materia(materia_id):
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, materia_id FROM conteudos WHERE materia_id =? 
          """, materia_id)
        
        linhas = cursor.fetchall()

        #converter as linhas em objetos, o sql devolve linhas e precisa ser convrtido em um objeto

        conteudos = []
        for linha in linhas:
            conteudo = Conteudo(id = linha[0], nome = linha[1], materia_id = linha[2])
            conteudos.append(conteudo)

        conexao.close()
        return conteudos
    
    def atualizar_conteudo():
        pass
    def excluir_conteudo():
        pass