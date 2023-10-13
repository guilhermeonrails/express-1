import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Gourmet', 'aberto': None},
    {'nome': 'Cantina da Nonna', 'categoria': 'Italiana', 'aberto': True},
    {'nome': 'Sushi', 'categoria': 'Japonesa', 'aberto': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'aberto': False}
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

def calcular_espacamento_entre_elementos_de_uma_lista(lista, chave):
    return max(len(item[chave]) for item in lista) + 1

def opcao_invalida():
    print(f'{cor_vermelho}{"❌ Opção inválida"}{reset_cor}')
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
    # tamanho_maximo = max(len(restaurante['nome']) for restaurante in restaurantes)
    # tamanho_maximo_categoria = max(len(restaurante['categoria']) for restaurante in restaurantes)

    tamanho_maximo_nome = calcular_espacamento_entre_elementos_de_uma_lista(restaurantes, 'nome')
    tamanho_maximo_categoria = calcular_espacamento_entre_elementos_de_uma_lista(restaurantes, 'categoria')
    
    print(f'{cor_verde}{"Restaurantes".ljust(tamanho_maximo_nome)} | {"Categoria".ljust(tamanho_maximo_categoria)} | Aberto{reset_cor}')

    for restaurante in restaurantes:
        nome = restaurante['nome'].ljust(tamanho_maximo_nome)
        categoria = restaurante['categoria'].ljust(tamanho_maximo_categoria)
        aberto = '✔️' if restaurante['aberto'] else '☐'
        print(f"{nome} | {categoria.upper()} | ⇒ {aberto}")

    input('\nPressione enter para voltar ')

def ativar_restaurante():
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
        print(f'{cor_vermelho}❌ Restaurante não encontrado{reset_cor}')
    
    input('\nPressione enter para voltar ao menu e escolha uma opção válida! ')

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
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
            break
        else:
            opcao_invalida()
    except:
        opcao_invalida()