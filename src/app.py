import streamlit as st
from database import criar_tabela, inserir_produto, listar_produtos, atualizar_quantidade, remover_produto

criar_tabela()

st.title("Sistema de Controle de Estoque")
st.write("Bem-vindo ao sistema!")



st.subheader("Cadastrar novo produto")

if "form_key" not in st.session_state:
    st.session_state.form_key = 0

nome = st.text_input("Nome do produto", key=f"nome_{st.session_state.form_key}")
preco = st.number_input("Preço", min_value=0.0, key=f"preco_{st.session_state.form_key}")
quantidade = st.number_input("Quantidade", min_value=0, step=1, key=f"quantidade_{st.session_state.form_key}")

if st.button("Cadastrar produto"):
    try:
        inserir_produto(nome, preco, quantidade)
        st.success("Produto cadastrado com sucesso!")
        st.session_state.form_key += 1 #muda a chave indentificadora, assim limpa a caixa de texto
        st.rerun()
    except ValueError as erro:
        st.error(f"Erro: {erro}")



st.subheader("Produtos cadastrados")

produtos = listar_produtos()

if not produtos:
    st.info("Nenhum produto cadastrado")
else:
    st.table(produtos)



st.subheader("Atualizar quantidade")

id_atualizar = st.number_input("ID do produto", min_value=1, step=1, key="id_atualizar")
nova_quantidade = st.number_input("Nova quantidade", min_value=0, step=1, key="nova_quantidade")

if st.button("Atualizar quantidade"):
    try:
        atualizar_quantidade(id_atualizar, nova_quantidade)
        st.success("Quantidade atualizada com sucesso!")
        st.rerun()
    except ValueError as erro:
        st.error(f"Erro: {erro}")


st.subheader("Remover produto")

id_remover = st.number_input("ID do produto a ser removido", min_value=1, step=1, key="id_remover")

if st.button("Remover produto"):
    try:
        remover_produto(id_remover)
        st.success("Produto removido com sucesso!")
        st.rerun()
    except ValueError as erro:
        st.error(f"Erro: {erro}")