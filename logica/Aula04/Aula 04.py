inicio: int = int(input('Digite o número inicial: '))
fim: int = int(input('Digite o número final: '))
soma: int = 0

print(f'Somando todos os números pares entre {inicio} e {fim}...')

for i in range(inicio, fim+1):
    if i % 2 == 0: 
        soma += i

if soma > 0:
    print(f'O resultado foi: {soma}.')
else:
    print(f'Ops... Não há números pares entre {inicio} e {fim}.')
    