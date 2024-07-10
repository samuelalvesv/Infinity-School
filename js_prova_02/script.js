function obter_classificacao(imc) {
    let classificacao;
    
    switch (true) {
        case (imc < 16):
            classificacao = 'Baixo peso muito grave';
            break;
        case (imc >= 16 && imc <= 16.99):
            classificacao = 'Baixo peso grave';
            break;
        case (imc >= 17 && imc <= 18.49):
            classificacao = 'Baixo peso';
            break;
        case (imc >= 18.50 && imc <= 24.99):
            classificacao = 'Peso normal';
            break;
        case (imc >= 25 && imc <= 29.99):
            classificacao = 'Sobrepeso';
            break;
        case (imc >= 30 && imc <= 34.99):
            classificacao = 'Obesidade grau I';
            break;
        case (imc >= 35 && imc <= 39.99):
            classificacao = 'Obesidade grau II';
            break;
        case (imc >= 40):
            classificacao = 'Obesidade grau III';
            break;
        default:
            classificacao = 'Classificação desconhecida';
    }

    return classificacao
}

let div_resultado = document.getElementById('resultado')

function Calcular(){
    let nome = document.getElementById('txt_nome').value
    let altura_cm = Number(document.getElementById('txt_altura').value)
    let peso = (Number(document.getElementById('txt_peso').value)).toFixed(2)

    if (!nome || !altura_cm || !peso) {
        alert("Por favor, preencha todos os campos corretamente.");
        return;
    }

    let altura_mt = (altura_cm / 100).toFixed(2)

    let imc = (peso / (altura_mt ** 2)).toFixed(2)

    let classificacao = obter_classificacao(imc)

    let resposta = (`<p>Olá, ${nome}, segue o resultado do seu IMC:<br>
        Altura: ${altura_mt}m | Peso: ${peso}kg <br><br> IMC: ${imc} | Status: ${classificacao}</p>`)

    div_resultado.innerHTML = resposta
}

