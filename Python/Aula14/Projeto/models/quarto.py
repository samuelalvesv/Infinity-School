from enum import Enum
from data import db

def novo_id():
    db.quartos.count() + 1

class TipoQuarto(Enum):
    SINGLE = 1
    DOUBLE = 2
    SUITE = 3

class SatusDisponibilidade(Enum):
    DISPONIVEL = 1
    OCUPADO = 2

class Quarto:
    def __init__(self, numero, tipo: TipoQuarto, preco_diaria, status: SatusDisponibilidade):
        self.Id = novo_id()
        self.Numero = numero
        self.Tipo: TipoQuarto = tipo
        self.Preco_Diaria = preco_diaria
        self.Status: SatusDisponibilidade = status

    def __str__(self):
        return (f"Quarto {self.Id}: Número: {self.Numero} | Status: {self.Status} | Tipo: {self.Tipo} | Preço da diaria: R$ {self.Preco_Diaria}")
    