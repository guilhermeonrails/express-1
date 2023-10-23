class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.aberto = False

    def alternar_estado(self):
        return not self.aberto

restaurante_sushi = Restaurante(nome='Sushi', categoria='Japonesa')
print(type(restaurante_sushi.nome))
print(restaurante_sushi.nome.__class__) # exibe a classe str
print(dir(restaurante_sushi)) # Em Python, você pode ver todos os métodos de uma classe utilizando a função dir() ou acessando o atributo __dict__ da classe. 
print(restaurante_sushi.__dict__) # Obtém um dicionário com todos os métodos e atributos da classe

# print(dir(Restaurante))    
# print(type(Restaurante))