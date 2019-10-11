#%% Criando classes
class Programa: # Classe mãe
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa): # classe filha
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # invocamos o __init__ da classe mãe com super()
        self._duracao = duracao

class Serie(Programa): # classe filha
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) # invocamos o __init__ da classe mãe com super()
        self._temporadas = temporadas

#%%
f1 = Filme('Vingadores', 2018, 160)
s1 = Serie('Atlanta', 2005, 5)

print(f'{f1.nome}. Likes: {f1._likes}')
f1.likes
print(f'{f1.nome}. Likes: {f1._likes}')

s1.likes
s1.likes
print(f'{s1.nome}. Likes: {s1._likes}')