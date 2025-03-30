class Item {
  Nome: string
  Quantidade: number
  PrecoUnitario: number

  constructor(nome: string, quantidade: number, precoUnitario: number) {
    (this.Nome = nome),
      (this.Quantidade = quantidade),
      (this.PrecoUnitario = precoUnitario)
  }
}

class Pedido {
  Itens: Item[]

  constructor(itens: Item[]) {
    this.Itens = itens
  }
}

function PrecoTotal(pedido: Pedido): number {
  let total: number = 0;

  for (const element of pedido.Itens) {
    total += element.PrecoUnitario * element.Quantidade;
  }

  return total;
}

let bolo: Item = new Item("Bolo", 2, 10);
let pao: Item = new Item("Item", 5, 1);

let pedido: Pedido = new Pedido([bolo, pao]);

let total: number = PrecoTotal(pedido);

console.log(total);
