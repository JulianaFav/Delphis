import sqlite3
from models.study_session import SessaoEstudos

class ServiceSessaoEstudos:
    def criar_sessao(sessao):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()
         cursor.execute("""
            INSERT INTO sessoes_estudos (duracao, data, conteudo_id) VALUES(?,?,?)

         """,(sessao.duracao, sessao.data, sessao.conteudo_id))

         sessao.id = cursor.lastrowid
         conexao.commit()
         conexao.close()
         return sessao
    def alterar():
        pass
    def listar_todas():
        pass
    def listar_por_data():
        pass
    def listar_por_conteudo():
        pass
    def excluir():
        pass
