import sqlite3

def inserir_produto(nome, preco, quantidade):
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


if __name__ == "__main__":
    criar_tabela()

    remover_produto(5)
    produtos = listar_produtos()
    print(produtos)