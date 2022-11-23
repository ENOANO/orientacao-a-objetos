from model import Produto, Loja, RegistroDeEstoque

agua_tonica = Produto("Tônica", 15.00, 5.43, "Água Tonificada")
maca = Produto("Fazenda", 5.00, 1.33, "Maça")

loja = Loja()
loja.adicionarAoEstoque(RegistroDeEstoque(100, agua_tonica))
loja.adicionarAoEstoque(RegistroDeEstoque(500, maca))

print(loja.exibirEstoque())