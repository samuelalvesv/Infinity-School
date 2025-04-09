--[PYIA-A15] Crie uma tabela chamada Clientes com as colunas ID, Nome, Idade e Cidade. Defina a coluna ID como a chave primária e autoincrementável.

    CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME VARCHAR(500) NOT NULL,
    IDADE INTEGER,
    CIDADE VARCHAR(100)
    )

COMMIT