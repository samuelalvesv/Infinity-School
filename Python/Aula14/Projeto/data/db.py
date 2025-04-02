from models.cliente import Cliente
from models.quarto import Quarto, TipoQuarto, SatusDisponibilidade
from models.reserva import Reserva, StatusReserva
from models.gerenciador_de_reserva import GerenciadorDeReservas

clientes: list[Cliente] = []
quartos: list[Quarto] = []
reservas: list[Reserva] = []
