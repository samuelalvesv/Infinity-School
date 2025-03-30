import { textChangeRangeIsUnchanged } from "typescript";

function somar(a: number, b: number): void{
    console.log(a + b)
}

//somar(7,8)

function saudar(nome: string, saudacao?: string): void{
    console.log(`${saudacao || 'Olá'}, ${nome}`)
}

//saudar('Samuel')
//saudar('Samuel', 'Bom dia')

function saudar2(nome: string, saudacao: string = 'Olá'): void{
    console.log(`${saudacao}, ${nome}`)
}

//saudar2('Samuel')
//saudar2('Samuel', 'Bom dia')


//Funções anonimas
const dividir = (a: number, b: number): number => a / b;

//console.log(dividir(4,2))

const aluno: {nome: string, idade: number, nota:number} = {
    nome: "Lucas",
    idade: 20,
    nota: 8.5
}

//console.log(aluno)

//Interface
interface Pessoa{
    nome: string
    idade: number
}

let samuel: Pessoa = {
    nome: 'Samuel',
    idade: 27
}

//console.log(samuel)

interface Funcionario extends Pessoa{
    salario: number
}

let funcSamuel: Funcionario = {
    nome: "Samuel",
    idade: 27,
    salario: Infinity
}

//console.log(funcSamuel)

interface IBichinhoVirtual{
    Tempo:number

    dormir(): void,
    acordar(): void,
    brincar(tempo: number): void,
    comer(comida: string): void
}

class BixinhoVirtual implements IBichinhoVirtual{
    Tempo: number

    constructor(tempo: number){
        this.Tempo = tempo
    }

    dormir(): void {
        console.log("Dormiu");
    }
    acordar(): void {
        console.log("Acordou")
    }
    brincar(): void {
        console.log(`Brincando por ${this.Tempo} minutos`)
    }
    comer(comida: string): void {
        console.log(`Comendo ${comida}`)
    }
}

let tamagoxi = new BixinhoVirtual(10)

tamagoxi.acordar()
tamagoxi.dormir()
tamagoxi.brincar()
tamagoxi.comer("Sanduiche")

