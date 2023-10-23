class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def alternar_estado(self):
        return not self.ativo
    
    def __str__(self):
        return f'Restaurante: {self.nome} | Categoria: {self.categoria}'

restaurante_praca = Restaurante(nome='Praca', categoria='Gourmet')
restaurante_sushi = Restaurante('Sushi', 'Japonesa')
restaurante_pizza = Restaurante('Pizza Suprema', 'Pizza')

restaurantes = [restaurante_praca, restaurante_sushi, restaurante_pizza]
