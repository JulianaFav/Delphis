import sqlite3

def criar_banco():
    conexao = sqlite3.connect('delphis.db')
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome  TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conteudos(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nome TEXT NOT NULL,
         materia_id INTEGER,
         FOREIGN KEY (materia_id) REFERENCES materias(id) ON DELETE CASCADE                 
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessoes_estudos(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     duracao INTEGER NOT NULL,
     data TEXT NOT NULL,
     conteudo_id INTEGER,
     FOREIGN KEY (conteudo_id) REFERENCES conteudos(id) ON DELETE CASCADE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS atividades(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     qtd_total INTEGER NOT NULL,
     qtd_acertos INTEGER NOT NULL, 
     percentual REAL,
     data TEXT NOT NULL,
     conteudo_id INTEGER,
     FOREIGN KEY (conteudo_id) REFERENCES conteudos(id) ON DELETE CASCADE                  
    )
    """)



    conexao.commit()
    conexao.close()

criar_banco()