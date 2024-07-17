function fatorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    } else {
        return n * fatorial(n - 1);
    }
  }
  
  function fibonacci(n) {
    let seq = [0, 1];
    for (let i = 2; i <= n; i++) {
      seq.push(seq[i - 1] + seq[i - 2]);
    }
    return seq.slice(0, n);
}

function Calcular(){
    let txt_numero = parseInt(document.getElementById('txt_numero').value)
    
    let div_resultado = document.getElementById('resultado')
    div_resultado.innerHTML = ''; 
    
    let resultado_fatorial = fatorial(txt_numero)
    let resultado_fibonacci = fibonacci(txt_numero)

    let resultado = `Dado o número ${txt_numero}, seu fatorial é ${resultado_fatorial} e a sequência de Fibonacci até ele é ${resultado_fibonacci}`

    let paragrafo = document.createElement('p')
    paragrafo.innerHTML = resultado
    div_resultado.appendChild(paragrafo)
}