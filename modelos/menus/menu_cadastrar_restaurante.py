from modelos.menus.menu import Menu
from modelos.restaurante import Restaurante, restaurantes

class RegistrarRestaurante(Menu):
    def __init__(self):
        super().exibir_subtitulos('Adicionar restaurante')
        nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input(f'Qual a categoria do restaurante {nome_restaurante}: ')
        dados_novo_restaurante = Restaurante(nome_restaurante, categoria)
        restaurantes.append(dados_novo_restaurante)
        super().exibir_opcoes()