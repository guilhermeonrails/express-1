import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': None},
    {'nome': 'Pizza Suprema do Universo', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

cor_vermelho = "\033[41m"
cor_azul = "\033[34m"
cor_verde = "\033[32m"
reset_cor = "\033[0m"

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''')

def exibir_opcoes():
    print('► 1. Adicionar restaurante')
    print('► 2. Listar restaurantes')
    print('► 3. Ativar restaurante')
    print('► 4. Sair\n')

def finalizar_app():
    os.system('clear')
    exibir_subtitulos('Finalizando o programa')

def validar_opcao_do_menu():
    return int(input('Escolha uma opção: '))

def opcao_invalida():
    print(f'{cor_vermelho}❌ Opção inválida{reset_cor}\n')
    input('Pressione enter e escolha uma opção válida')

def exibir_subtitulos(texto):
    os.system('clear')
    linha = '*' * (len(texto) + 4)
    texto_personalizado = f' {texto} ' 
    print(linha)
    print(texto_personalizado)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Adicionando restaurantes')
    nome_do_restaurante =input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)

    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!')
    input('\nPressione enter para voltar ao menu principal ')

def calcular_espacamento_maximo(lista):
    espacamento_maximo = {}

    for restaurante in lista:
        for chave, valor in restaurante.items():
            if isinstance(valor, str):
                tamanho = len(valor)
                if chave not in espacamento_maximo or tamanho > espacamento_maximo[chave]:
                    espacamento_maximo[chave] = tamanho + 2

    return espacamento_maximo

def listar_restaurantes():
    exibir_subtitulos('Listando restaurantes')
    espacamentos = calcular_espacamento_maximo(restaurantes)
    
    print(f"{cor_azul}{'Restaurante'.ljust(espacamentos['nome'])} | {'Categoria'.ljust(espacamentos['categoria'])} | {'Ativo'}{reset_cor}")
    
    for restaurante in restaurantes:
        nome = restaurante['nome'].ljust(espacamentos['nome'])
        categoria= restaurante['categoria'].ljust(espacamentos['categoria'])
        ativo = '✔' if restaurante['ativo'] else '☒'
        print(f'{nome} | {categoria} | {ativo}')

    input('\nPressione enter para voltar ao menu principal ')

while True:
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()

    try:
        opcao_escolhida = validar_opcao_do_menu()
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
            break
        else:
            opcao_invalida()
    except:
        opcao_invalida()