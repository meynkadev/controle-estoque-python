from database import criar_tabela, listar_produtos, inserir_produto, atualizar_quantidade, remover_produto

if __name__ == "__main__":
    criar_tabela()

    while True:
        print("\n=== Sistema de Controle de Estoque ===")
        print("\n1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Atualizar produtos")
        print("4. Remover produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Encerrando sistema...")
            break

        elif opcao == "1":
            try:
                nome = input("Nome do produto: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
            
                inserir_produto(nome, preco, quantidade)
                print("Produto cadastrado com sucesso!")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            produtos = listar_produtos()
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                for produto in produtos:
                    print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]} | Quantidade: {produto[3]}")

        elif opcao == "3":
            try:
                id_produto = int(input("ID do produto: "))
                nova_quantidade = int(input("Nova quantidade: "))
                atualizar_quantidade(id_produto, nova_quantidade)
                print("Quantidade atualizada com sucesso!")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            try:
                id_produto = int(input("Digite o ID do produto que deseja remover: "))
                remover_produto(id_produto)
                print("Produto removido com sucesso!")
            except ValueError as erro:
                print(f"Erro: {erro}")
        else:
            print("Opção ínválida.")





    
