import sqlite3
from models.study_session import SessaoEstudos

class ServiceSessaoEstudos:
    def criar_sessao(sessao):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         if sessao.duracao <= 0:
           raise ValueError("Duração inválida")

         cursor.execute("""
            INSERT INTO sessoes_estudos (duracao, data, conteudo_id) VALUES(?,?,?)
         """,(sessao.duracao, sessao.data, sessao.conteudo_id))

         sessao.id = cursor.lastrowid
         conexao.commit()
         conexao.close()
         return sessao
    def alterar(sessao):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         if sessao.duracao <= 0:
           raise ValueError("Duração inválida")
         
         cursor.execute("""
            UPDATE sessoes_estudos
            SET duracao = ?, data = ?, conteudo_id = ?
            WHERE id = ?
            """, (sessao.duracao, sessao.data, sessao.conteudo_id, sessao.id))
         
         if cursor.rowcount == 0:
            print("Nenhuma sessao foi atualizada")

         conexao.commit()
         conexao.close()

    def listar_todas():
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         cursor.execute("""
            SELECT * 
            FROM sessoes_estudos
         """)

         linhas = cursor.fetchall()
         sessoes = []
         for linha in linhas:
            sessao = SessaoEstudos(id = linha[0], duracao = linha[1], data = linha[2], conteudo_id = linha[3])
            sessoes.append(sessao)

         conexao.close()
         return sessoes
    def listar_por_data(data):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         cursor.execute("""
            SELECT * 
            FROM sessoes_estudos
            WHERE data = ?
         """, (data,))

         linhas = cursor.fetchall()
         sessoes = []
         for linha in linhas:
            sessao = SessaoEstudos(id = linha[0], duracao = linha[1], data = linha[2], conteudo_id= linha[3])
            sessoes.append(sessao)

         conexao.close()
         return sessoes
    def listar_por_conteudo(conteudo_id):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         cursor.execute("""
            SELECT * 
            FROM sessoes_estudos
            WHERE conteudo_id = ?
         """, (conteudo_id,))

         linhas = cursor.fetchall()
         sessoes = []
         for linha in linhas:
            sessao = SessaoEstudos(id = linha[0], duracao = linha[1], data = linha[2], conteudo_id= linha[3])
            sessoes.append(sessao)

         conexao.close()
         return sessoes
    def excluir(id):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         cursor.execute(""" 
          DELETE FROM sessoes_estudos
          WHERE id = ?""", (id,))
         
         if cursor.rowcount == 0:
            print("Nenhuma sessao foi excluída")
        
         conexao.commit()
         conexao.close()
