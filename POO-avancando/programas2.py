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
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self.duracao} min - {self._likes}'

class Serie(Programa): # classe filha
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) # invocamos o __init__ da classe mãe com super()
        self.temporadas = temporadas
        # self.__str__() # só para deixar mil grau

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self.temporadas} temporadas - {self._likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
    
    def tamanho(self):
        return len(self.programas)
#%% Criando objetos
f1 = Filme('Vingadores', 2018, 160)
s1 = Serie('Atlanta', 2005, 5)

print(f'{f1.nome}. Likes: {f1._likes}')
f1.likes
print(f'{f1.nome}. Likes: {f1._likes}')

s1.likes
s1.likes
print(f'{s1.nome}. Likes: {s1._likes}')

#%% Criando lista e print de atributos
filmes_e_series = [f1, s1]
for programa in filmes_e_series:
    # verificar se tem atibuto duracao ou temporadas (hasattr)
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas # ternario 
    print(f'{programa.nome} - {detalhes} D - {programa._likes}')

#%% Criando lista e print de um novo jeito
filmes_e_series = [f1, s1]
for programa in filmes_e_series:
    print(programa) # polimorfismo

#%% Mais filmes e criando uma playlist
f1 = Filme('Vingadores', 2018, 160)
f2 = Filme('João e Maria', 2015, 100)
s1 = Serie('Atlanta', 2005, 5)
s2 = Serie('Breaking Bad', 2013, 5)

lista_programas = [f1, f2, s1, s2]

p1 = Playlist('Playlist do André', lista_programas)
print(f'Programas: {p1.tamanho()}')
for p in p1.programas:
    print(p)