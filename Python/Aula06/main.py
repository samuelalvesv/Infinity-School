from ModelTarefa import Tarefa
import Menu

escolha = int(input(Menu.MenuPrincipal()))

if escolha == 1:
    Tarefa.AdicionarTarefa()
elif escolha == 2:
    Tarefa.ListarTaredas()
elif escolha == 3:
    Tarefa.ConcluirTarefa()
elif escolha == 4:
    Tarefa.ExcluirTarefa()
elif escolha == 5:
    Tarefa.ListarTaredasPorPrioridade()
elif escolha == 6:
    Tarefa.ListarTarefasPorCategoria()

