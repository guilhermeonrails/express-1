from modelos.restaurante import Restaurante

restaurante_nonna = Restaurante('cantina da Nonna', 'Italiana')
restaurante_praca = Restaurante('praça', 'Salgados')
restaurante_sushi= Restaurante('Sushi', 'Japonesa')
restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()