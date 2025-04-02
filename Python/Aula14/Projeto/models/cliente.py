from data import db

def novo_id():
    db.clientes.count() + 1

class Cliente:
    def __init__(self, nome, telefone, email):
        self.Id = novo_id()
        self.Nome = nome
        self.Telefone = telefone
        self.Email = email

    def __str__(self):
        return (f"Cliente {self.Id}: Nome: {self.Nome} | Telefone: {self.Telefone} | E-mail: {self.Email}")
    