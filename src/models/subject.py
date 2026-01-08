#models é oq o sistema é
#models não falam com o banco, e sim o service

class Materia:
    def __init__(self, nome, id = None):
        self.nome = nome 
        self.id = id
