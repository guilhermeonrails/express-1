from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

mc = Restaurante('McDonalds', 'FastFood')
mc.adicionar_prato_no_cardapio('Hamburger', 39.90, 'teste')

# lasanha = Prato('Lasanha', 100, 'A melhor lasanha da vida com muito queijo')
# lasanha.aplicar_desconto()

# suco = Bebida('Suco de Laranja', 10, 500)
# suco.aplicar_desconto()

def main():
    print(mc.exibir_cardapio)

if __name__ == "__main__":
    main()