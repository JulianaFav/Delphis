class Conteudo:
    def __init__(self, nome, materia_id, id=None):
        self.id = id
        self.nome = nome
        self.materia_id = materia_id

    def __str__(self): #faz com que o python converta em texto
        return self.nome