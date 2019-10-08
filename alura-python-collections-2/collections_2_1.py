#%% Listas
x = [1,2,3,4]
y = [4,2,1,1,5,6]
x.extend(y) # união de listas

#%% Conjuntos
z = set(x) # conjuntos não entra elemento repetidos
# conjuntos não pssuem indexação

#%% União com conjuntos
x = [1,2,3,4]
x_set = set(x)
y_set = set(y)
x_set | y_set

#%% Intersecção com conjuntos
x_set & y_set

#%% Apenas em um conjunto
x_set - y_set

#%% OU exclusivo
x_set ^ y_set

#%% Conjuntos são mutaveis
x_set.add(23)
x_set

#%% Frozent (conjuntos congelados) - não da para modificar
x_frozen = frozenset(x)

#%% Exemplo
texto = 'Meu nome é André. Eu gosto de cachorros e gosto de nome de cachorros'
texto_split = texto.split()
texto_set = set(texto_split)
texto_set

#%% Dicionario
x_dict = {
            'a': 1,
            'b': 2,
            'c': 3
}

x_dict['a']

x_dict.get('d',0) # Se a chave não existir, retorna zero

#%% Modificando dicionario
x_dict = {
            'a': 1,
            'b': 2,
            'c': 3
}

x_dict['d'] = 4 # adicionando uma chave nova ao dicionado
del x_dict['c'] # removendo uma chave do dicionario
x_dict

#%% Consultar dicionario
'a' in x_dict
'd' in x_dict

#%% loop em dicionario (chaves)
for elemento in x_dict:
    print(elemento)

#%% loop em dicionario (valores)
for elemento in x_dict.values():
    print(elemento)

#%% loop em dicionario (itens)
for k,v in x_dict.items():
    print(f'{k} = {v}')

#%% List comprehension
lista_palavras = [f'palavra {chave}' for chave in x_dict]
lista_palavras

#%% Contador usando package de collections
from collections import Counter
texto = ''' Meu nome é André Arruda. Tenho 24 anos. Sou desenvolvedor em Harpia Health Solutions.
            Gosto de programar em matlab e python, mas estou tentando sempre aprender uma coisa nova.
            Fiz crossfit durante um tempom, mas estourei o pé e o joelho. Agora estou mais calmo e só corro 
            meia maratona (21km) quando dá kkkkkk. Desafios sempre são bons para termos conquistas.'''

aparicoes = Counter(texto.lower())
total_caracteres = sum(aparicoes.values())
proporcoes = [(caractere, 100*frequencia/total_caracteres) for caractere, frequencia in aparicoes.items()]
proporcoes

#%% Contador exibindo os dez mais comuns
from collections import Counter
texto = ''' Meu nome é André Arruda. Tenho 24 anos. Sou desenvolvedor em Harpia Health Solutions.
            Gosto de programar em matlab e python, mas estou tentando sempre aprender uma coisa nova.
            Fiz crossfit durante um tempom, mas estourei o pé e o joelho. Agora estou mais calmo e só corro 
            meia maratona (21km) quando dá kkkkkk. Desafios sempre são bons para termos conquistas.'''

aparicoes = dict(Counter(texto.lower()).most_common(10))
total_caracteres = sum(aparicoes.values())
proporcoes = [(caractere, 100*frequencia/total_caracteres) for caractere, frequencia in aparicoes.items()]
for caractere, frequencia in proporcoes:
    print(f'" {caractere} " => {frequencia:.2f}%')

