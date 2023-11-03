class Estabelecimento:
    def __init__(self, nome, tipo_de_cozinha, descricao):
        self._nome = nome
        self._tipo_de_cozinha = tipo_de_cozinha
        self._descricao = descricao

    def exibir_detalhes(self):
        print(f'{self._nome} | {self._tipo_de_cozinha} | {self._descricao}')

        
        