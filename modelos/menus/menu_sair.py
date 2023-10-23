from modelos.menus.menu import Menu

class MenuSair(Menu):
    
    def __init__(self):
        super().exibir_subtitulos('Finalizando o app')
         # Usando 'super()' para chamar o método da classe pai