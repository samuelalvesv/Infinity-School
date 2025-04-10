# [PYIA-A13] Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. 
# O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. 
# Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. 
# Crie um método depositar que permita adicionar um valor ao saldo, um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), 
# e um método exibir_saldo que exiba o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, 
# garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular

    def depositar(self, valor: float):
        if valor <= 0:
            print('O valor para deposito deve ser maior que zero.')
            return
        
        self._saldo += valor

        print(f'Deposito realizado com sucesso. Saldo Atual: R$ {self._saldo}')
        
    def sacar(self, valor: float):
        if self._saldo < valor:
            print('Saldo insuficiente para o valor do saque.')
            return
        
        self._saldo -= valor

        print(f'Saque realizado com sucesso. Saldo Atual: R$ {self._saldo}')
        
    def exibir_saldo(self):
        print(f'Saldo Atual: R$ {self._saldo}')

conta_samuel: ContaBancaria = ContaBancaria(0, 'Samuel')

conta_samuel.exibir_saldo()
conta_samuel.depositar(105)
conta_samuel.sacar(200)
conta_samuel.sacar(20)

    