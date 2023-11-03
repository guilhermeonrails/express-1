from modelos.avaliacao import Avaliacao
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    @property
    def ativo(self):
        return '✔️' if self._ativo else '☐'

    @classmethod
    def listar_restaurantes(cls):
        print(f'\n{"Restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(19)} | Ativo')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)}| {restaurante.ativo}')
        print()

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    def adicionar_bebida_no_cardapio(self, nome, preco, tamanho):
        item_para_adiconar = Bebida(nome, preco, tamanho)
        self._cardapio.append(item_para_adiconar)

    def adicionar_prato_no_cardapio(self, nome, preco, descricao):
        item_para_adiconar = Prato(nome, preco, descricao)
        self._cardapio.append(item_para_adiconar)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            print(f'{i}. Nome: {item.nome}\n   Preço: R$ {item.preco:.2f}\n   Descrição: {item.descricao}\n' if hasattr(item, 'descricao') else f'{i}. Nome: {item.nome}\n   Preço: R$ {item.preco:.2f}\n   Tamanho: {item.tamanho} ml\n')

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        media_das_notas = round(sum(avaliacao._nota for avaliacao in self._avaliacoes) / len(self._avaliacoes), 1)
        return media_das_notas