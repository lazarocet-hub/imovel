class Imovel:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def exibir(self):
        return f"Imovel: {self.nome} | Aluguel: R$ {self.valor}"


imovel1 = Imovel("Casa Centro", 1500)

print(imovel1.exibir())