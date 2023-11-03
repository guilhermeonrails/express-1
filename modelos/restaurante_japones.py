from modelos.restaurante import Estabelecimento

class RestauranteJapones(Estabelecimento):

    def __init__(self, nome, tipo_de_cozinha, descricao):
        super().__init__(nome, tipo_de_cozinha, descricao)
        
    def servir_especialidade(self, especialidade):
        print(f'Prato especial do dia: {especialidade}')