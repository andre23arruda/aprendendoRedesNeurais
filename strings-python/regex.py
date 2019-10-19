#%% Expressões regulares
import re # modulo de regex

email1 = 'meu numero eh 1234-1234'
email2 = "fale comigo em 1234-1234, esse é meu telefone"
email3 = '1234-1234 é meu celular'
email4 = 'jfoweg 9999-9898'
email4 = 'ajeohag 89859-9898 ahsfkashkf'
email5 = 'ajeohag 89859-9898 ahsfkashkf 1234-6666'
email6 = 'ajeohag 898599898 ahsfkashkf 1234-6666'

padrao = '[0123456789][0123456789][0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]'
padrao2 = '[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'
padrao3 = '[0-9]{4}-[0-9]{4}'
padrao4 = '[0-9]{4,5}-[0-9]{4}'
padrao5 = '[0-9]{4,5}[-]*[0-9]{4}' # com ou sem hifen

retorno1 = re.search(padrao, email1) # encontra padrao
print(f'{retorno1.group()}')

retorno4 = re.search(padrao2, email4) # encontra padrao
print(f'{retorno4.group()}')

retorno4 = re.search(padrao3, email2) # encontra padrao
print(f'{retorno4.group()}')

retorno4 = re.search(padrao4, email4) # encontra padrao
print(f'{retorno4.group()}')

retorno5 = re.findall(padrao4,email5)
print(retorno5)

retorno6 = re.findall(padrao5,email6)
print(retorno6)


