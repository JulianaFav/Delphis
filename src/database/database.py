import sqlite3

def criar_banco():
    conexao = sqlite3.connect('delphis.db')
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
         FOREIGN KEY (materia_id) REFERENCES materias(id)                  
    )
    """)



    conexao.commit()
    conexao.close()

criar_banco()