from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return f'{self.nome} | {self.preco:.2f} | {self.descricao}'
    
    def aplicar_desconto(self):
       self.preco -= (self.preco * 0.08)
