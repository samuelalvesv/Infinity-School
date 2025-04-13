import { writeFileSync, readFileSync } from "fs"

class Funcionario {
    matricula: number
    nome: string
    salario: number

    constructor(matricula: number, nome: string, salario: number) {
        this.matricula = matricula
        this.nome = nome
        this.salario = salario
    }

    exibirDados(){
        console.log('\n---Dados do funcionário---')
        console.log(`Nome: ${this.nome}`)
        console.log(`Matricula: ${this.matricula}`)
        console.log(`Salário: ${this.salario}\n`)
    }
}

class Professor extends Funcionario {
    turmas: string[]

    constructor(matricula: number, nome: string, salario: number, turmas: string[]) {
        super(matricula, nome, salario)
        this.turmas = turmas        
    }

    override exibirDados(): void {
        console.log('\n---Dados do professor---')
        console.log(`Nome: ${this.nome}`)
        console.log(`Matricula: ${this.matricula}`)
        console.log(`Salário: ${this.salario}`)
        console.log(`Turmas: ${this.turmas}\n`)
    }
}

class Coordenador extends Funcionario {
}

class Diretor extends Funcionario {
}

let p1 = new Professor(123, 'Samuel', 9500, ['Matematica', 'Portugues'])

// console.log(p1)
// p1.exibirDados()


//-------------------------------------------------------------------------

class Aluno{
    matricula: number
    nome: string
    nota: number
    curso: string

    constructor(matricula: number, nome: string, nota: number, curso: string) {
        this.matricula = matricula
        this.nome = nome
        this.nota = nota
        this.curso = curso
    }

}

interface Repositorio{
    cadastrar(aluno: Aluno): void
}

class InMemoryRepositorio implements Repositorio{
    alunos: Aluno[] = []
    cadastrar(aluno: Aluno): void {
        this.alunos.push(aluno)
        console.log('Aluno cadastrado com sucesso!')
    }
}

class jsonRepositorio implements Repositorio{
    alunos: Aluno[] = []

    cadastrar(aluno: Aluno): void {
        this.alunos.push(aluno)
        let dados = JSON.stringify(this.alunos)
        writeFileSync('dados.json', dados, 'utf-8')
        console.log('Aluno cadastrado com sucesso"')
    }
}

let aluno1 = new Aluno(1, 'Samuel', 9, 'TypeScript')
let aluno2 = new Aluno(1, 'Teste', 10, 'Python')
// let repositorio = new InMemoryRepositorio()
let repositorio = new jsonRepositorio()
repositorio.cadastrar(aluno1)
repositorio.cadastrar(aluno2)
console.log(repositorio.alunos)

