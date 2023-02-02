from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = "Barra de Chocolate Premiada"
    nome_da_empresa = "Willy Wonka's Factory"
    data_de_fabricacao = "01/01/2023"
    data_de_validade = "31/12/2023"
    numero_de_serie = "0000001"
    instrucoes_de_armazenamento = "Após aberto, vá recolher seu prêmio"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento
        )

    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
