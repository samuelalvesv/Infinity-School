class Tarefa:
    def __init__(self, nome, descricao, prioridade, categoria):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.concluida = False

    def __str__(self):
        return (f"Nome: {self.nome}, \ndescricao: {self.descricao}, "
                f"\nprioridade: {self.prioridade}, \ncategoria: {self.categoria}, "
                f"\nConluída: {"sim" if self.concluida else "não"}\n\n")
    