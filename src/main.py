from database import criar_tabela, listar_produtos, inserir_produto, atualizar_quantidade, remover_produto

if __name__ == "__main__":
    criar_tabela()
    produtos = listar_produtos()
    print(produtos)

    try:
        inserir_produto("Teste", -5, 10)
    except ValueError as erro:
        print(f"Erro ao inserir produto: {erro}")  
    produtos = listar_produtos()
    print(produtos)

    try:
        atualizar_quantidade(-1, 10)
    except ValueError as erro:
        print(f"Erro ao atualizar quantidade: {erro}")
    produtos = listar_produtos()
    print(produtos)

    try:
        remover_produto(-1)
    except ValueError as erro:
            print(f"Erro ao remover produto: {erro}")
    produtos = listar_produtos()
    print(produtos)