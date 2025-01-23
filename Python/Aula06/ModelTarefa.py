from Repositorio import database

class Tarefa:
    def __init__(self, nome, descricao, prioridade, categoria):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.concluida = False

    def __string__(self):
        return (f"Tarefa(nome={self.nome}, descricao={self.descricao}, "
                f"prioridade={self.prioridade}, categoria={self.categoria})")
    
    def AdicionarTarefa():
        tarefa = Tarefa(input("Nome da tarefa: "),
                        input("Descrição da tarefa: "),
                        int(input("Prioridade da tarefa [1 a 10]: ")),
                        input("Categoria da tarefa: "))

        database.append(tarefa)

    def ListarTaredas():
        for tarefa in database:
            print(tarefa)

    def ConcluirTarefa(tarefa):
        tarefa.concluida = True

    def ExcluirTarefa():
        database.remove(Tarefa)

    def ListarTaredasPorPrioridade():
        pass

    def ListarTarefasPorCategoria():
        pass