-- SQLite
--[PYIA-A16] Crie uma tabela chamada Produtos que contenha quatro colunas: ProdutoID, NomeProduto, Quantidade e Preco. 
--A coluna ProdutoID deve ser um identificador único para cada produto, a coluna NomeProduto deve armazenar o nome do produto, 
--a coluna Quantidade deve indicar a quantidade disponível do produto, e a coluna Preco deve representar o preço do produto. 
--Após criar a tabela, insira três registros diferentes, cada um representando um produto distinto, incluindo valores específicos 
--para ProdutoID, NomeProduto, Quantidade e Preco.

CREATE TABLE IF NOT EXISTS Produtos (
    ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeProduto TEXT,
    Quantidade INTEGER,
    Preco REAL

INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ('PS5', 10, 4500)
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ('Xbox one S', 20, 2500)
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ('Nitendo Switch', 2, 300)

