class Produto:
    def __init__(self, marca, tamanho, preco, nome):
        self.marca = marca
        self.tamanho = tamanho
        self.preco = preco
        self.nome = nome
    
    def calcularDesconto(self, porcentagem):
        resultado = (self.preco*porcentagem)/100
        return self.preco - resultado

class RegistroDeEstoque:
    def __init__(self, quantidade, produto: Produto) -> None:
        self.quantidade = quantidade
        self.produto = produto

    def __repr__(self):
        return "\n"+str(self.produto.nome) + " \n" + "Quantidade: " + str(self.quantidade)+"\n"
    
class Loja:
    def __init__(self):
        self.estoque = []

    def adicionarAoEstoque(self, registroDeEstoque: RegistroDeEstoque):
        self.estoque.append(registroDeEstoque)

    def exibirEstoque(self):
        return self.estoque