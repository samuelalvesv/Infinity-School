from data import db
from models.quarto import Quarto, SatusDisponibilidade
from models.reserva import Reserva, StatusReserva

class GerenciadorDeReservas:
    def verificar_disponibilidade(quarto: Quarto):
        if quarto.Status == SatusDisponibilidade.DISPONIVEL:
            return True
        return False
    
    def criar_reserva(model: Reserva):
        db.reservas = model

    def modificar_reserva(model: Reserva):
        reserva = next((r for r in db.reservas if r.id == model.id), None)

        if not reserva:
            return 'Reserva não encontrada.'

        reserva.Cliente = model.Cliente
        reserva.Quarto = model.Quarto
        reserva.Data_Checkin = model.Data_Checkin
        reserva.Data_Checkout = model.Data_Checkout
        reserva.Status = model.Status

        return 'Reserva alterado com sucesso.'
    
    def cancelar_reserva(model: Reserva):
        reserva = next((r for r in db.reservas if r.id == model.id), None)
        
        if not reserva:
            return 'Reserva não encontrada.'
        
        reserva.Status = StatusReserva.CANCELADA
        reserva.Quarto.Status = SatusDisponibilidade.DISPONIVEL
        
        return 'Reserva cancelada com sucesso.'
