class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        return round(((self.nota1 + self.nota2 + self.nota3) / 3), 2)
    
    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"
    
    def __str__(self):
        return f"""
Nome: {self.nome}

Nota 1: {self.nota1}
Nota 2: {self.nota2}
Nota 3: {self.nota3}

Média: {self.media()}

Situação: {self.situacao()}
"""

lista_alunos = []

qtde_alunos = int(input('Digite a quantidade de alunos: '))

for c in range(qtde_alunos):
    aluno = Aluno(nome = input("\nDigite o nome do aluno: "),
                  nota1 = float(input("\nDigite a primeira nota: ")),
                  nota2 = float(input("Digite a segunda nota: ")),
                  nota3 = float(input("Digite a última nota: ")))
    
    lista_alunos.append(aluno)

print("\n\nEXIBINDO A LISTA DE ALUNOS CADASTRADOS\n")

for aluno in lista_alunos:    
    print(aluno)
