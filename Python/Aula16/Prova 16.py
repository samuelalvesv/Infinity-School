import sqlite3

# Como criar um banco de dados no sqlite
db = sqlite3.connect('estoque.db')
cursor = db.cursor()

cursor.execute(
  	'''
	CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeProduto TEXT,
        Quantidade INTEGER,
        Preco REAL
    )
	'''
)
db.commit()

cursor.execute(
  	'''
	INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ('PS5', 10, 4500)
	'''
)
db.commit()

cursor.execute(
  	'''
	INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ('Xbox one S', 20, 2500)
	'''
)
db.commit()

cursor.execute(
  	'''
	INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ('Nitendo Switch', 2, 300)
	'''
)
db.commit()