try:
    numero: float = float(input("Digite um número: "))

    if numero > 0:
        print(f"O número {numero} é positivo")
    elif numero == 0:
        print(f"O número {numero} é zero, logo é nulo")
    else:
        print(f"O número {numero} é negativo")
except:
    print("Carácter inválido.")