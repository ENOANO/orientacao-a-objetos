class Produto:
    def __init__(self, marca, tamanho, preco, nome):
        self.marca = marca
        self.tamanho = tamanho
        self.preco = preco
        self.nome = nome
    
    def calcularDesconto(self, porcentagem):
        resultado = (self.preco*porcentagem)/100
        return self.preco - resultado
    
    #faça um metodo para comparaar se o nome e a marca do produto são iguias a do objeto que ele está comparando. 

class RegistroDeEstoque:
    def __init__(self, quantidade, produto: Produto) -> None:
        self.quantidade = quantidade
        self.produto = produto

    def __repr__(self):
        return "\n"+str(self.produto.nome) + " \n" + "Quantidade: " + str(self.quantidade)+"\n"
    
    #Faço um metodo de removerDoEstoque, passando o produto e subtraindo 1 da quantidade do registro

class Loja:
    def __init__(self):
        self.estoque = []

    def adicionarAoEstoque(self, registroDeEstoque: RegistroDeEstoque):
        self.estoque.append(registroDeEstoque)

    def exibirEstoque(self):
        return self.estoque

    #Faça um metodo que possibilidade encontrar um produto da Atributo estoque
    #Faça um metodo de vender que deve receber como parametro um produto e SUBTRAIR 1 do Registro de Estoque