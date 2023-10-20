import os
from models.restaurante import Restaurante

restaurante_praca = Restaurante(nome='Praça', categoria='Gourmet')
restaurante_nonna = Restaurante(nome='Nonna', categoria='Italiana')
restaurante_sushi = Restaurante(nome='Sushi', categoria='Japonesa')
restaurante_pizza = Restaurante(nome='Pizza Supreme', categoria='Pizza')

restaurantes = [restaurante_praca, restaurante_nonna, restaurante_sushi, restaurante_pizza]

cor_vermelho = "\033[41m"
cor_azul = "\033[34m"
cor_verde = "\033[32m"
cor_padrao = "\033[0m"

def exibir_nome_do_programa():
    print('''Sabor express''')

def finalizar_app():
    exibir_subtitulos('Finalizando o app')

def exibir_subtitulos(texto):
    os.system('clear')
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

def calcular_espacamento():
    return max((len(restaurante.nome) for restaurante in restaurantes)) + 2, max((len(restaurante.categoria) for restaurante in restaurantes)) + 2

def opcao_invalida():
    print(f'{cor_vermelho}{"❌ Opção inválida"}{cor_padrao}')
    input('\nPressione enter para voltar ao menu e escolha uma opção válida! ')

def cadastrar_restaurante():
    exibir_subtitulos('Adicionar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Qual a categoria do restaurante {nome_restaurante}: ')
    dados_novo_restaurante = Restaurante(nome_restaurante, categoria)
    restaurantes.append(dados_novo_restaurante)

def listar_restaurantes():
    exibir_subtitulos('Listando restaurantes')
    espacamento_nome, espacamento_categoria = calcular_espacamento()
    
    print(f'{cor_verde}{"Restaurantes".ljust(espacamento_nome)} | {"Categoria".ljust(espacamento_categoria)} | Aberto{cor_padrao}')

    for restaurante in restaurantes:
        nome = restaurante.nome.ljust(espacamento_nome)
        categoria = restaurante.categoria.ljust(espacamento_categoria)
        aberto = '✔️' if restaurante.aberto else '☐'
        print(f"{nome} | {categoria.upper()} | ⇒ {aberto}")

    input('\nPressione enter para voltar ')

def ativar_restaurante():
    exibir_subtitulos('Ativação de restaurante')
    nome_restaurante_para_ativar = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante_para_ativar == restaurante.nome:
            restaurante.aberto = restaurante.alternar_estado()
            print(restaurante.aberto)
            mensagem = f'O {restaurante.nome} foi ativado com sucesso!' if restaurante.aberto else f'O {restaurante.nome} foi desativado com sucesso!'
            print(mensagem)
            restaurante_encontrado = True
            break
            
    if not restaurante_encontrado:
        print(f'{cor_vermelho}❌ Restaurante não encontrado{cor_padrao}')
    
    input('\nPressione enter para voltar ao menu e escolher uma opção válida! ')

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