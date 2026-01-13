class Atividade:
    def __init__(self, nome, qtd_total, qtd_acertos, data, conteudo_id, id = None, percentual=None):
        self.id = id
        self.nome = nome 
        self.qtd_total = qtd_total
        self.qtd_acertos = qtd_acertos
        self.conteudo_id = conteudo_id
        self.percentual = percentual
        self.data = data