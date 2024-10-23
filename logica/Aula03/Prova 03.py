numero_secreto: int = 7
chute: int = 0
tentativas: int = 3

while (numero_secreto != chute) and (tentativas > 0):
    tentativas -= 1

    chute = int(input('Tente adivinhar o número secreto: '))

    if numero_secreto == chute:
        print(f'Parabéns você acertou! O nuúmero secreto era {numero_secreto}.')
    else:
        if tentativas > 0:
            print(f'Tente novamente, você tem mais {tentativas} tentativa. Você consegue!')
        else:
            print('Game over, as tentativas acabaram.')

    