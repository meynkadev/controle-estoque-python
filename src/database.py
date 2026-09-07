import sqlite3

def inserir_produto(nome, preco, quantidade):
    if not isinstance(nome, str) or nome.strip() == "":
        raise ValueError("O nome do produto deve ser um texto não vazio")

    if not isinstance(preco, (int, float)) or preco <= 0:
        raise ValueError("O preço deve ser um número maior que zero")

    if not isinstance(quantidade, int) or quantidade <= 0:
        raise ValueError("A quantidade deve ser um número inteiro maior ou igual a zero")
    
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade)
        VALUES (?, ?, ?)
    """, (nome, preco, quantidade))
    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos

def atualizar_quantidade(id, quantidade):
    if not isinstance(id, int) or id <= 0:
        raise ValueError("O id deve ser um número inteiro maior que zero")

    if not isinstance(quantidade, int) or quantidade < 0:
        raise ValueError("A quantidade deve ser um número inteiro maior ou igual a zero")

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
    """, (quantidade, id))
    conexao.commit()
    conexao.close()

def remover_produto(id):
    if not isinstance(id, int) or id <= 0:
        raise ValueError("O valor do id deve ser um inteiro maior que zero.")

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM produtos
        WHERE id = ?
    """, (id,))
    conexao.commit()
    conexao.close()

def criar_tabela():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()
