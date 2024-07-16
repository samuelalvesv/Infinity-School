function Lancar(){
    let quantidade = parseInt(document.getElementById('txt_qtde').value)
    
    let div_resultado = document.getElementById('resultado')
    div_resultado.innerHTML = ''; 
    
    for (let index = 0; index < quantidade; index++) {
        const alunoLabel = document.createElement('label')
        alunoLabel.textContent = `Nota aluno nº ${index + 1}: `
        
        const alunoInput = document.createElement('input')
        alunoInput.type = 'number';
        alunoInput.id = `nota_aluno_${index + 1}`
        alunoInput.placeholder = 'Digite a nota'
        
        const alunoContainer = document.createElement('div')
        alunoContainer.appendChild(alunoLabel)
        alunoContainer.appendChild(alunoInput)
        
        div_resultado.appendChild(alunoContainer)
    }

    const btn_calcular = document.createElement('button')
    btn_calcular.textContent = 'Calcular'
    btn_calcular.onclick = Calcular
    btn_calcular.id = 'btn_calcular'
    div_resultado.appendChild(btn_calcular)
}

function Calcular(){
    let div_resultado = document.getElementById('resultado')
    const resumoContainer = document.createElement('div')
    resumoContainer.innerHTML = ''
    
    let quantidade = parseInt(document.getElementById('txt_qtde').value)
    let menor = Infinity, maior = -Infinity, total = 0, media = 0
    
    for (let index = 0; index < quantidade; index++) {
        let nota = Number(document.getElementById(`nota_aluno_${index + 1}`).value)
        
        total += nota
        
        if (menor > nota) {menor  = nota.toFixed(2)}
        if (maior < nota) {maior = nota.toFixed(2)}
    }
    
    media = (total / quantidade).toFixed(2)
    
    const resumo = document.createElement('p')
    resumo.innerHTML = `A média da turma foi ${media}, a menor nota foi ${menor} e a maior nota da turma foi ${maior}`
    resumoContainer.appendChild(resumo)
    
    div_resultado.appendChild(resumoContainer)

}