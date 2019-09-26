#%% range
x = ['hue','78','oi',3]
for i in range(len(x)):
    print(f'{i},{x[i]}')

#%% in list
usuarios = [('andre',24,1995),
            ('joao',25,1994)]
for nome,idade,ano in usuarios
    print(f'{nome},{idade},{ano}')

#%% posso desempacotar apenas um cara da tupla
for nome,_,_ in usuarios:
    print(nome)