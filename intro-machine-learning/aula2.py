import pandas as pd

dados = pd.read_csv(r'dados/tracking.csv')
treino_x = dados['home','how_it_works','contact']
