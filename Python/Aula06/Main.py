import RepositoryTask
import Menu

escolha = -1

while escolha != 0:
    escolha = int(input(Menu.MenuPrincipal()))

    if escolha == 1:
        RepositoryTask.AdicionarTarefa()
    elif escolha == 2:
        RepositoryTask.ListarTaredas()
    elif escolha == 3:
        RepositoryTask.ConcluirTarefa()
    elif escolha == 4:
        RepositoryTask.ExcluirTarefa()
    elif escolha == 5:
        RepositoryTask.ListarTaredasPorPrioridade()
    elif escolha == 6:
        RepositoryTask.ListarTarefasPorCategoria()
