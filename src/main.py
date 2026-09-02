from database import criar_tabela, listar_produtos

if __name__ == "__main__":
    criar_tabela()
    produtos = listar_produtos()
    print(produtos)