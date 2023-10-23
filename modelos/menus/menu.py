import os

class Menu:
    def exibir_nome_do_programa(self):
        os.system('clear')
        print('''Sabor Express\n''')
    
    def exibir_opcoes(self):
        self.exibir_nome_do_programa()
        print('➤ 1. Adicionar nova restaurante')
        print('➤ 2. Listando restaurantes')
        print('➤ 3. Ativar restaurantes')
        print('➤ 4. Sair\n')

    def exibir_subtitulos(self, texto):
        os.system('clear')
        linha = '*' * (len(texto) + 4)
        texto_personalizado = f' {texto} ' 
        print(linha)
        print(texto_personalizado)
        print(linha)
        print()

    def escolher_opcao(self):
    opcoes = {
        1: RegistrarRestaurante,
        2: listat_restaurantes,
        3: alternar_estado_restaurante
        4: MenuSair,
    }

    