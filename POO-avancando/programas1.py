#%% Criando classes
class Filme(Programa): # classe filha
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__likes = 0
        self.__duracao = duracao

    @property
    def likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie: # classe filha
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0
        
    @property
    def likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


#%%
f1 = Filme('Vingadores', 2018, 160)
s1 = Serie('Atlanta', 2005, 5)

print(f'{f1.nome}. Likes: {f1._Filme__likes}')
f1.likes
print(f'{f1.nome}. Likes: {f1._Filme__likes}')

s1.likes
s1.likes
print(f'{s1.nome}. Likes: {s1._Serie__likes}')

