from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Salgados')

restaurante_praca.alternar_estado()

restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Ana', 2)
restaurante_praca.receber_avaliacao('Maria', 3)

restaurante_praca.adicionar_bebida_no_cardapio('Coca-Cola',5, 350)
restaurante_praca.adicionar_bebida_no_cardapio('Pepsi',4.5, 350)

restaurante_praca.adicionar_prato_no_cardapio('Hamburgão', 5, 'Um hambúrguer saboroso com carne, queijo, alface e tomate.')
restaurante_praca.adicionar_prato_no_cardapio('Pizza Margherita', 20, 'Uma pizza clássica com molho de tomate, muçarela e manjericão.')
restaurante_praca.adicionar_prato_no_cardapio('Macarrão à Carbonara', 18, 'Macarrão com molho à base de ovos, queijo parmesão e bacon.')



def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()