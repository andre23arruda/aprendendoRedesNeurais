#%% Criando classe 
class ExtratorUrl:
    def __init__(self, url):
        self.isOK(url)
    
    @property
    def isEmpty(self):
        return False if self.url else True

    def isOK(self,url):
        if url and url.startswith('https://bytebank.com'):
            print('URL válida')
            self.url = url
        else:
            self.url = ''
            print('URL inválida')

    def __len__(self): # método especial para retornar tamanho 
        return len(self.url)

    def __str__(self):
        texto = f'Origem: {(self.extraiArgumentos())[0]} \
                \nDestino: {(self.extraiArgumentos())[1]} \
                \nValor: {(self.extraiArgumentos())[2]} \n'
        return texto

    def __eq__(self, outro): # método para comparar objetos
        return self.url == outro.url

    def extraiArgumentos(self):
        if not self.isEmpty:
            i1 = self.url.find('=') + 1
            i2 = self.url.find('&',i1+1)

            i3 = self.url.find('=',i2+1) + 1
            i4 = self.url.find('&',i3+1)

            i5 = self.url.find('=',i4+1) + 1

            moedaOrigem = self.url[i1:i2]
            moedaDestino = self.url[i3:i4]
            valor = self.url[i5:]

            return moedaOrigem, moedaDestino, valor

#%% Testando
s1 = ExtratorUrl('huehuehuehu')
print(s1.isEmpty)

s2 = ExtratorUrl('')
print(s2.isEmpty)

#%% URL
url = 'https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700'

url_object = ExtratorUrl(url)
print(url_object.extraiArgumentos())

print(f'{len(url_object)}')

print(url_object)

#%% Comparando dois objetos
url1 = 'https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700'
url_object1 = ExtratorUrl(url1)

url2 = 'https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700'
url_object2 = ExtratorUrl(url2)

url3 = 'https://bitebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700'
url_object3 = ExtratorUrl(url3)

print(url_object1 == url_object2)
print(url_object1 == url_object3)














