# [PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
# Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.

produtos = {}
valor_total = 0

for i in range(0,5):
    nome_produto = input("Nome do produto: " )
    valor_produto = float(input("Informe o valor: R$ "))
    
    valor_total += valor_produto

    produtos[nome_produto] = valor_produto

print(f'Produtos no carrinho:\n{produtos}\nValor total: R$ {valor_total}')
