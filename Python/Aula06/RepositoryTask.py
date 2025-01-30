from ModelTask import Tarefa
import os

database = [
    Tarefa("Comprar mantimentos", "Ir ao supermercado para comprar alimentos", 9, "Casa")
    ,Tarefa("Fazer exercícios", "Exercitar-se por pelo menos 30 minutos", 6, "Saúde")
    ,Tarefa("Lavar a louça", "Lavar e secar a louça acumulada", 5, "Casa")
]

def AdicionarTarefa():
    os.system('cls')
    print('Adicionando tarefa:\n')

    tarefa = Tarefa(input('Nome da tarefa: '),
                    input('Descrição da tarefa: '),
                    int(input('Prioridade da tarefa [1 a 10]: ')),
                    input('Categoria da tarefa: '))

    database.append(tarefa)

    print('\nTarefa adicionada com sucesso!\n')
    input('\nDigite qualquer tecla para continuar...')

def ListarTaredas():
    os.system('cls')
    print('Listando todas as tarefas:\n')

    i = 1
    for tarefa in database:
        print(f'Tarefa {i}: {tarefa}')
        i += 1

    input('\nDigite qualquer tecla para continuar...')

def ConcluirTarefa():
    os.system('cls')
    print('Finalizando tarefa:\n')

    name = input("Digite o nome da tarefa que deseja finalizar: ")
    for tarefa in database:
        if tarefa.nome == name:
            tarefa.concluida = True
            print('\nTarefa concluida com sucesso!\n')
            break
    
    input('\nDigite qualquer tecla para continuar...')

def ExcluirTarefa():
    os.system('cls')
    print('Excluindo tarefa:\n')

    name = input("Digite o nome da tarefa que deseja excluir: ")
    for tarefa in database:
        if tarefa.nome == name:
            database.remove(Tarefa)
            print('\nTarefa excluida com sucesso!\n')
            break
    
    input('\nDigite qualquer tecla para continuar...')

def ListarTaredasPorPrioridade():
    os.system('cls')
    print('Exibindo tarefas ordenada por prioridade:\n')

    tasks_sorted = sorted(database, key=lambda task: task.prioridade, reverse=True)

    i = 1
    for tarefa in tasks_sorted:
        print(f'Tarefa {i}: {tarefa}')
        i += 1

    input('\nDigite qualquer tecla para continuar...')

def ListarTarefasPorCategoria():
    os.system('cls')
    print('Exibindo tarefas ordenada por categoria:\n')

    tasks_sorted = sorted(database, key=lambda task: task.categoria)

    i = 1
    for tarefa in tasks_sorted:
        print(f'Tarefa {i}: {tarefa}')
        i += 1
    input('\nDigite qualquer tecla para continuar...')
