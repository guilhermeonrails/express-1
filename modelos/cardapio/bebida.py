from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida():
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

    