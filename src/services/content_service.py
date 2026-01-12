import sqlite3
from models.content import Conteudo

class ContentService:
    def listar_por_materia(materia_id):
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, materia_id 
            FROM conteudos 
            WHERE materia_id =?

          """, (materia_id))
        
        linhas = cursor.fetchall()

        #converter as linhas em objetos, o sql devolve linhas e precisa ser convrtido em um objeto

        conteudos = []
        for linha in linhas:
            conteudo = Conteudo(id = linha[0], nome = linha[1], materia_id = linha[2])
            conteudos.append(conteudo)

        conexao.close()
        return conteudos
    
    def criar_conteudo(conteudo):
        conexao = sqlite3.connect('delphis.db')
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO conteudos ( nome, materia_id) VALUES (?, ?)
            """, (conteudo.nome, conteudo.materia_id))
        
        conteudo.id = cursor.lastrowid # id que o banco de dados gerou 
        conexao.commit()
        conexao.close()
        return conteudo

    def deletar(conteudo_id):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()

         cursor.execute("""
            DELETE FROM conteudos 
            WHERE id = ? 
         """, (conteudo_id))

         conexao.commit()
         conexao.close()

    def atualizar(conteudo_id, novo_nome):
         conexao = sqlite3.connect('delphis.db')
         conexao.execute("PRAGMA foreign_keys = ON")
         cursor = conexao.cursor()
         
         cursor.execute("""
            UPDATE conteudos
            SET nome = ?
            WHERE id = ?
            """, (novo_nome, conteudo_id)
        )
         
         conexao.commit()
         conexao.close()
        