db_alunos = []

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Ana Silva",
    "idade": "20",
    "curso": "Ciência da Computação"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Carlos Oliveira",
    "idade": "22",
    "curso": "Engenharia Civil"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Mariana Souza",
    "idade": "21",
    "curso": "Medicina"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "João Pereira",
    "idade": "23",
    "curso": "Direito"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Luiza Costa",
    "idade": "19",
    "curso": "Psicologia"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Felipe Almeida",
    "idade": "24",
    "curso": "Arquitetura"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Isabela Martins",
    "idade": "22",
    "curso": "Educação Física"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Gabriel Rodrigues",
    "idade": "20",
    "curso": "Engenharia Elétrica"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Camila Santos",
    "idade": "21",
    "curso": "Biologia"
})

db_alunos.append({
    "matricula": len(db_alunos) + 1,
    "nome": "Rafael Pereira",
    "idade": "23",
    "curso": "Administração"
})

def menu():
    escolha = ''

    while escolha not in (0,1,2,3):
        try:
            escolha = int(input("""\nDigite uma das opções:
    [1] - Cadastrar aluno
    [2] - Listar alunos cadastrados
    [3] - Pesquisar aluno
    [0] - Sair\n"""))
        except:
            continue

    if (escolha == 0):
        print("\nFechando sistema...\n")

    elif(escolha == 1):
        cadastro_novo_aluno()
        
    elif(escolha == 2):
        exibir_alunos()
        
    elif(escolha == 3):
        pesquisar_alunos()

def cadastro_novo_aluno():
    aluno = {"matricula": len(db_alunos) + 1,
        "nome": input("Nome do aluno: "),
        "idade": input("Idade: "),
        "curso": input("Curso: ")}
    
    db_alunos.append(aluno)

    print(f"""\nAluno cadastrado:
Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}""")
    
    input("\nEnter para continuar.")
    menu()

def exibir_alunos():
    print("Alunos matrículados:\n")
    for aluno in db_alunos:
        print(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")

    input("\nEnter para continuar.")
    menu()

def pesquisar_alunos():
    consulta = input("\nPesquisa: ").upper()

    alunos_encontrados = 0

    for aluno in db_alunos:
        if(str(aluno['matricula']).__contains__(consulta) or
           aluno['nome'].upper().__contains__(consulta) or
           aluno['idade'].upper().__contains__(consulta) or
           aluno['curso'].upper().__contains__(consulta)):
            
            alunos_encontrados += 1
            print(f"\nMatrícula: {aluno['matricula']} | Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")

    if alunos_encontrados == 0:
        print('\nEssa consulta não retornou nenhum resultado')
            
    input("\nEnter para continuar.")
    menu()

menu()


