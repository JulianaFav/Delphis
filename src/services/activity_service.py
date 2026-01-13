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

         if atividade.nome == None:
             atividade.nome = 'Atividade sem nome'

         cursor.execute("""
            INSERT INTO atividades (nome, qtd_total, qtd_acertos, data, percentual, conteudo_id) VALUES(?,?,?,?,?,?)
          """,(atividade.nome,
                atividade.qtd_total, atividade.qtd_acertos, atividade.data,
                atividade.percentual, 
                atividade.conteudo_id ) )

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

         if atividade.nome == None:
             atividade.nome = 'Atividade sem nome'

         cursor.execute("""
          UPDATE atividades
          SET nome = ?, qtd_total = ?, qtd_acertos = ?, data = ?, percentual = ?, conteudo_id = ? 
          WHERE id = ?
          """, (atividade.nome, atividade.qtd_total, atividade.qtd_acertos, atividade.data, atividade.percentual, atividade.conteudo_id, atividade.id ))
         
         if cursor.rowcount == 0:
            print("Nenhuma atividade foi atualizada")
         conexao.commit()
         conexao.close()
         

    def excluir_atividade(id):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         cursor.execute(""" 
          DELETE FROM atividades
          WHERE id = ?""", (id,))
         
         if cursor.rowcount == 0:
            print("Nenhuma atividade foi excluída")
        
         conexao.commit()
         conexao.close()
        

    def listar_todas():
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT *
            FROM atividades
        """)
        linhas = cursor.fetchall()
        atividades = []
        for linha in linhas:
            atividade = Atividade(id = linha[0], nome = linha[1], qtd_total = linha[2], qtd_acertos = linha[3], percentual = linha[4], data = linha[5], conteudo_id = linha[6])
            atividades.append(atividade)

        conexao.close()
        return atividades

    def listar_por_conteudo(conteudo_id):
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT *
            FROM atividades
            WHERE conteudo_id = ?
        """, (conteudo_id,))
        linhas = cursor.fetchall()
        atividades = []
        for linha in linhas:
            atividade = Atividade(id = linha[0], nome = linha[1], qtd_total = linha[2], qtd_acertos = linha[3], percentual = linha[4], data = linha[5], conteudo_id = linha[6])
            atividades.append(atividade)

        conexao.close()
        return atividades
    def listar_atividade_data(data):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         cursor.execute("""
            SELECT *
            FROM atividades
            WHERE data = ?
        """, (data,))
         linhas = cursor.fetchall()
         atividades = []
         for linha in linhas:
            atividade = Atividade(id = linha[0], nome = linha[1], qtd_total = linha[2], qtd_acertos = linha[3], percentual = linha[4], data = linha[5], conteudo_id = linha[6])
            atividades.append(atividade)

         conexao.close()
         return atividades