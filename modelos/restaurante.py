from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
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

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        media_das_notas = round(sum(avaliacao._nota for avaliacao in self._avaliacoes) / len(self._avaliacoes), 1)
        return media_das_notas