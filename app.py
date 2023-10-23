from modelos.restaurante import restaurantes
from modelos.menus.menu import Menu
from modelos.menus.menu_sair import MenuSair
from modelos.menus.menu_cadastrar_restaurante import RegistrarRestaurante

cor_vermelho = "\033[41m"
cor_azul = "\033[34m"
cor_verde = "\033[32m"
cor_padrao = "\033[0m"

def calcular_espacamento():
    return max((len(restaurante.nome) for restaurante in restaurantes)) + 2, max((len(restaurante.categoria) for restaurante in restaurantes)) + 2

def opcao_invalida():
    print(f'{cor_vermelho}{"❌ Opção inválida"}{cor_padrao}')
    input('\nPressione enter para voltar ao menu e escolha uma opção válida! ')
    main()

def listar_restaurantes():
    exibir_subtitulos('Listando restaurantes')
    espacamento_nome, espacamento_categoria = calcular_espacamento()
    
    print(f'{cor_verde}{"Restaurantes".ljust(espacamento_nome)} | {"Categoria".ljust(espacamento_categoria)} | Ativo{cor_padrao}')

    for restaurante in restaurantes:
        nome = restaurante.nome.ljust(espacamento_nome)
        categoria = restaurante.categoria.ljust(espacamento_categoria)
        ativo = '✔️' if restaurante.ativo else '☐'
        print(f"{nome} | {categoria.upper()} | ⇒ {ativo}")

    input('\nPressione enter para voltar ')
    main()

def alternar_estado_restaurante():
    exibir_subtitulos('Ativação de restaurante')
    nome_restaurante_para_ativar = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False  # Variável para rastrear se o restaurante foi encontrado
    
    for restaurante in restaurantes:
        if nome_restaurante_para_ativar == restaurante.nome:
            restaurante.ativo = restaurante.alternar_estado()
            mensagem = f'O {nome_restaurante_para_ativar} foi ativado com sucesso!' if restaurante.ativo else f'O {nome_restaurante_para_ativar} foi desativado com sucesso!'
            print(mensagem)
            restaurante_encontrado = True
            break  # Saia do loop assim que encontrar o restaurante
            
    if not restaurante_encontrado:
        print(f'{cor_vermelho}❌ Restaurante não encontrado{cor_padrao}')
    
    input('\nPressione enter para voltar ao menu e escolha uma opção válida! ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            RegistrarRestaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
           MenuSair()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
        menu = Menu()
        menu.exibir_opcoes()
        escolher_opcao()

if __name__ == "__main__":
    main()