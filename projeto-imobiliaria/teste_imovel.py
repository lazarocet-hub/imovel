from imovel import Imovel

def test_imovel():
    imovel = Imovel("Apartamento", 2000)

    assert imovel.nome == "Apartamento"
    assert imovel.valor == 2000

    print("Teste executado com sucesso")


test_imovel()