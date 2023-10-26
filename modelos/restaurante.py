class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    @property
    def nome(self):
        return self._nome.title()

    @property
    def categoria(self):
        return self._categoria.upper()
    
    @property
    def ativo(self):
        return '✔️' if self._ativo else '☐'

    @classmethod
    def listar_restaurantes(cls):
        print(f'\n{"Restaurante".ljust(30)} | {"Categoria".ljust(30)} | Ativo\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(30)} | {restaurante.categoria.ljust(30)} | {restaurante.ativo}')
        print()

    def alternar_estado(self):
        self._ativo = not self._ativo