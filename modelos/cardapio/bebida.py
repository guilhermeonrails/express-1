from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    '''
    Classe que representa uma bebida no cardápio de um restaurante.

    Args:
        nome (str): O nome da bebida.
        preco (float): O preço da bebida.
        tamanho (int): O tamanho da bebida em mililitros.

    Attributes:
        tamanho (int): O tamanho da bebida em mililitros.

    Parent Class:
        Esta classe herda da classe ItemCardapio.

    '''

    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return f'{self.nome} | {self.preco:.2f} | {self.tamanho}ml'
    
    def aplicar_desconto(self):
       self.preco -= (self.preco * 0.05)

    