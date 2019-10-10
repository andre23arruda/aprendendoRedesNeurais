class Cliente:
    def __init__(self, nome, age):
        self.__nome = nome
        self.__idade = age
        
    @property # definindo uma propriedade do objeto. Não precisa chamar com parenteses
    def nome(self):
        return self.__nome.title() # Coloca a primeira letra do nome em maiusculo

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade