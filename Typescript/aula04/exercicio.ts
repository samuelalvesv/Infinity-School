class Veiculo{
    marca: string
    modelo: string
    cor: string
    ligado: boolean
    ano: number

    constructor(marca: string, modelo: string, cor: string, ligado: boolean, ano: number) {
        this.marca = marca
        this.modelo = modelo
        this.cor = cor
        this.ligado = ligado
        this.ano = ano
    }

    ligar(){
        this.ligado = true
        console.log ('O carro foi ligado!')
    }

    desligar(){
        this.ligado = false
        console.log ('O carro foi desligado!')
    }
}

class Carro extends Veiculo{
    numeroDePortar: number

    constructor(marca: string, modelo: string, cor: string, ligado: boolean, ano: number, numeroDePortar: number) {
        super(marca, modelo, cor, ligado, ano);
        this.numeroDePortar = numeroDePortar
    }
}

class Moto extends Veiculo{
    cilindradas: number

    constructor(marca: string, modelo: string, cor: string, ligado: boolean, ano: number, cilindradas: number) {
        super(marca, modelo, cor, ligado, ano);
        this.cilindradas = cilindradas
    }
}

let carro = new Carro('Toyota', 'Corola', 'Preto', true, 2025, 4)
carro.desligar()
console.log(carro)

let moto = new Moto('Yamaha', 'Fazer 250', 'Azul', true, 2024, 250)
moto.desligar()
console.log(moto)