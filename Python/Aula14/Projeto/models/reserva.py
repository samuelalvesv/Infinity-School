from enum import Enum
from models.cliente import Cliente
from models.quarto import Quarto
from data import db

def novo_id():
    db.reservas.count() + 1

class StatusReserva(Enum):
    ATIVA = 1
    CANCELADA = 2

class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto, data_checkin, data_checkout, status: StatusReserva):
        self.Id = novo_id()
        self.Cliente: Cliente = cliente
        self.Quarto: Quarto = quarto
        self.Data_Checkin = data_checkin
        self.Data_Checkout = data_checkout
        self.Status : StatusReserva = status

    def __str__(self):
        return (f"Reserva {self.Id}: Cliente: {self.Cliente.Nome} | Quarto: {self.Quarto.Numero} | Data Checkin: {self.Data_Checkin} | Data Checkout: {self.Data_Checkout} | Status: {self.Status}")
    