from modelos.restaurante import Restaurante

restaurante_nonna = Restaurante('cantina da Nonna', 'Italiana')
restaurante_praca = Restaurante('praça', 'Salgados')

restaurante_praca.alternar_estado()

restaurante_nonna.receber_avaliacao('Lais', 4)
restaurante_nonna.receber_avaliacao('Mariana', 1)
restaurante_nonna.receber_avaliacao('Gui', 1)

restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Ana', 2)
restaurante_praca.receber_avaliacao('Maria', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()