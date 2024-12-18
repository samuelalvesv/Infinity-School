# [PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números. 
# Para fazer isso, some os três números e, em seguida, divida o resultado por três. 
# Por fim, a função deve retornar o valor da média aritmética calculada.

def calcular_media(n1, n2, n3):
    if isinstance(n1, (int, float)) and isinstance(n2, (int, float)) and isinstance(n3, (int, float)):
        return (n1+n2+n3)/3
    else:
        raise Exception("O valor digitado não é válido")
        

media = calcular_media(2,9,10)

print(f'A média de 2 9 e 10 é: {media}')

