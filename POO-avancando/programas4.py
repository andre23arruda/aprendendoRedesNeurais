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


class Playlist(): 
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas 

    # duck typing
    def __getitem__(self, item): # decretamos que nosso objeto é iteravel, ou seja, pode usar in de iteração
        return self._programas[item]

    @property
    def tamanho(self):
        return len(self._programas)

    def __len__(self): # Para ver o tamanho do bojeto (parecido com lista)
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    

#%% Criando filmes e playlist
f1 = Filme('Vingadores', 2018, 160)
f2 = Filme('João e Maria', 2015, 100)
f3 = Filme('Spiderman', 2019, 230)

s1 = Serie('Atlanta', 2005, 5)
s2 = Serie('Breaking Bad', 2013, 5)

lista_programas = [f1, f2, s1, s2]

p1 = Playlist('Playlist do André', lista_programas)
print(f'Programas: {p1.tamanho}') # p1 tem atributos de list, por isso len funciona
for p in p1:
    print(p)

#%% Verificando sem tem objeto dentro de uma lista
print(f'f1 tá em playlist? {f1 in p1}')
f4 = Serie('DBZ', 1995, 8)
print(f'f3 tá em playlist? {f4 in p1}')
print(f'Programas: {len(p1)}')










