import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Gourmet', 'aberto': False},
    {'nome': 'Cantina da Nonna', 'categoria': 'Italiana', 'aberto': True},
    {'nome': 'Sushi', 'categoria': 'Japonesa', 'aberto': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'aberto': False}
]

cor_vermelho = "\033[41m"
cor_azul = "\033[34m"
cor_verde = "\033[32m"
cor_padrao = "\033[0m"

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def finalizar_app():
    os.system('clear')
    exibir_subtitulos('Finalizando o app')

def exibir_subtitulos(texto):
    linha = '*' * (len(texto) + 4)
    texto_personalizado = f' {texto} ' 
    print(linha)
    print(texto_personalizado)
    print(linha)
    print()

def exibir_opcoes():
    print('➤ 1. Adicionar nova restaurante')
    print('➤ 2. Listando restaurantes')
    print('➤ 3. Ativar restaurantes')
    print('➤ 4. Sair\n')

def calcular_espacamento(chave):
    return max((len(restaurante[chave]) for restaurante in restaurantes)) + 2

def opcao_invalida():
    print(f'{cor_vermelho}{"❌ Opção inválida"}{cor_padrao}')
    input('\nPressione enter para voltar ao menu e escolha uma opção válida! ')

def cadastrar_restaurante():
    os.system('clear')
    exibir_subtitulos('Adicionar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Qual a categoria do restaurante {nome_restaurante}: ')
    dados_novo_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'aberto': False}
    restaurantes.append(dados_novo_restaurante)

def listar_restaurantes():
    os.system('clear')
    exibir_subtitulos('Listando restaurantes')
    espacamento_nome = calcular_espacamento('nome')
    espacamento_categoria = calcular_espacamento('categoria')
    
    print(f'{cor_verde}{"Restaurantes".ljust(espacamento_nome)} | {"Categoria".ljust(espacamento_categoria)} | Aberto{cor_padrao}')

    for restaurante in restaurantes:
        nome = restaurante['nome'].ljust(espacamento_nome)
        categoria = restaurante['categoria'].ljust(espacamento_categoria)
        aberto = '✔️' if restaurante['aberto'] else '☐'
        print(f"{nome} | {categoria.upper()} | ⇒ {aberto}")

    input('\nPressione enter para voltar ')

def alternar_estado_restaurante():
    os.system('clear')
    exibir_subtitulos('Ativação de restaurante')
    nome_restaurante_para_ativar = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False  # Variável para rastrear se o restaurante foi encontrado
    
    for restaurante in restaurantes:
        if nome_restaurante_para_ativar == restaurante['nome']:
            restaurante['aberto'] = not restaurante['aberto']
            mensagem = f'O {nome_restaurante_para_ativar} foi ativado com sucesso!' if restaurante['aberto'] else f'O {nome_restaurante_para_ativar} foi desativado com sucesso!'
            print(mensagem)
            restaurante_encontrado = True
            break  # Saia do loop assim que encontrar o restaurante
            
    if not restaurante_encontrado:
        print(f'{cor_vermelho}❌ Restaurante não encontrado{cor_padrao}')
    
    input('\nPressione enter para voltar ao menu e escolha uma opção válida! ')

def main():
    while True:
        os.system('clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                cadastrar_restaurante()
            elif opcao_escolhida == 2:
                listar_restaurantes()
            elif opcao_escolhida == 3:
                alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                finalizar_app()
                break
            else:
                opcao_invalida()
        except:
            opcao_invalida()

if __name__ == "__main__":
    main()