#precisa ter: id, conteudo_id, tempo de estudos, data 

class SessaoEstudos:
    def __init__(self, duracao, data, conteudo_id, id = None):
        self.duracao = duracao
        self.data = data
        self.conteudo_id = conteudo_id
        self.id = id