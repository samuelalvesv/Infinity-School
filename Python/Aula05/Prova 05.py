# [PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. 
# Esta função deve comparar os três números e identificar qual deles é o maior. 
# Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois. 
# A função deve então retornar o maior número encontrado.

def maior_numero(n1, n2, n3):
    numeros = [n1, n2, n3]

    print(sorted(numeros)[len(numeros)-1])

maior_numero(1,9,5)
