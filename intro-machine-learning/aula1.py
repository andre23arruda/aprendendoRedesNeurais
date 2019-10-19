#%% Caracteríticas

# f1 -> pelo longo
# f2 -> perna curta
# f3 -> faz au-au
porco1 = [1, 0, 0]
porco2 = [0, 1, 0]
porco3 = [0, 1, 1]

dog1 = [1, 0, 1]
dog2 = [1, 1, 1]
dog3 = [0, 0, 1]

# colocando todas as caracteristicas em um conjunto de dados
treino_x = [porco1, porco2, porco3, dog1, dog2, dog3] # dados

# classe 1 -> porco
# classe 0 -> dog
treino_y = [1, 1, 1, 0, 0, 0] # labels

#%% Criando modelo de classificação
from sklearn.svm import LinearSVC # sklearn faz a mágica
modelo = LinearSVC() # iniciando modelo
modelo.fit(treino_x, treino_y) # inserindo dados e classes no modelo inicializado

#%% Classificando animal misterioso
animal_misterioso1 = [0, 1, 1]
animal_misterioso2 = [1, 1, 0]
animal_misterioso3 = [0, 0, 1]

teste_x = [animal_misterioso1, animal_misterioso2, animal_misterioso3]
teste_y = [0, 1, 0] # labels que já sabemos desses animais

previsoes = modelo.predict(teste_x)
print(previsoes)


#%% Calculando acurácia na mão
n_acerto = (previsoes == teste_y).sum()
tamanho_teste_x = len(teste_x)
taxa_acerto = n_acerto/tamanho_teste_x
print(f'Acerto: {taxa_acerto*100 :.2f}%')


#%% Calculando acurácia com sklearn.metrics
from sklearn import metrics # esse módulo já traz tudo para nós

taxa_acerto = metrics.accuracy_score(teste_y, previsoes)
print(f'Acerto: {taxa_acerto*100 :.2f}%')





