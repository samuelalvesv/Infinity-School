from models.cliente import Cliente
from models.quarto import Quarto, TipoQuarto, SatusDisponibilidade
from models.reserva import Reserva, StatusReserva
from models.gerenciador_de_reserva import GerenciadorDeReservas
from data import db

quarto: Quarto = Quarto(numero=1, tipo=TipoQuarto.SINGLE, preco_diaria=200, status=SatusDisponibilidade.OCUPADO)

print(quarto)

disponivel: bool = GerenciadorDeReservas.verificar_disponibilidade(quarto=quarto)

print(disponivel)