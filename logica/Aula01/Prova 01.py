class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    @property
    def area(self):
        return round(self.base * self.altura, 2)

retangulo = Retangulo(
    base = float(input("Digite a base do triângulo: ")),
    altura = float(input("Digite a baaltura do triângulo: "))
)

print(f"A área do retângulo de base {retangulo.base} e altura {retangulo.altura} é de: {retangulo.area}")