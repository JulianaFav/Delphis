import sqlite3
from models.activity import Atividade



class ActivityService:
    def criar_atividade(atividade):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         if atividade.qtd_total > 0:
            atividade.percentual =  (atividade.qtd_acertos / atividade.qtd_total) * 100
         else:
             atividade.percentual = 0
         cursor.execute("""
            INSERT INTO atividades (nome, qtd_total, qtd_acertos, data, percentual, conteudo_id) VALUES(?,?,?,?,?,?)
          """, (atividade.nome,
                atividade.qtd_total, atividade.qtd_acertos, atividade.data
                atividade.percentual, 
                atividade.conteudo_id ))

         atividade.id = cursor.lastrowid
         conexao.commit()
         conexao.close()
         return atividade

    def atualizar_atividade(atividade):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         if atividade.qtd_total > 0:
            atividade.percentual = (atividade.qtd_acertos / atividade.qtd_total) * 100
         else:
            atividade.percentual = 0

         cursor.execute("""
          UPDATE atividades
          SET nome = ?, qtd_total = ?, qtd_acertos = ?, data = ?, percentual = ?, conteudo_id = ? 
          WHERE id = ?
          """, (atividade.nome, atividade.qtd_total, atividade.qtd_acertos, atividade.data, atividade.percentual, atividade.conteudo_id, atividade.id ))
         
         conexao.commit()
         conexao.close()
         

    def excluir_atividade():
        pass
    def listar_todas_atividades():
        pass
    def listar_atividade_conteudo():
        pass