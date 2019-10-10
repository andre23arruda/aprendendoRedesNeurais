class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto {self}\n')
        self.__numero = numero # atributo privado
        self.__titular = titular # atributo privado
        self.saldo = saldo # atributo de boa
        self.__limite = limite
        self.__codigo_banco = '001'
        
    def extrato(self):
        print(f"Saldo de {self.saldo} do titular {self.__titular}\n")
        
    def deposita(self,valor):
        print(f'Depositado valor de {valor}')
        self.saldo += valor
        Conta.extrato(self)
        
#    # primeira versão do método saca
#    def saca(self,valor): 
#        if valor <= self.__limite + self.saldo:
#            print(f'Valor sacado de {valor}')
#            self.saldo -= valor
#            Conta.extrato(self)
#        else:
#            print(f'Valor passou do limite {self.__limite}')
      
        
    def __pode_sacar(self, valor): # método privado
        return valor <= self.__limite + self.saldo
    
    def saca(self,valor): 
        if self.__pode_sacar(valor):
            print(f'Valor sacado de {valor}')
            self.saldo -= valor
            Conta.extrato(self)
        else:
            print(f'{valor} passou do limite de R${self.__limite}')
        
    def transfere(self, valor, conta2):
        self.saldo -= valor
        conta2.saldo += valor
        print(f'{self.__titular} transferiu R$ {valor} para {conta2.__titular}')
        
    def eh_inadimplente(self): 
        # mas esse método tem que estar implementado em outra classe, aqui ele não faz sentido
        if self.saldo < -self.__limite:
            print(f'O {self.__titular} está devendo R${-self.__limite + self.saldo}')
        else:
            print(f'Tudo certo com {self.__titular}')
        
    def get_saldo(self): 
        # get é a nomenclatura para fornecer um atributo do objeto
        return self.saldo
        
    def set_limite(self, limite): 
        # set é a nomenclatura para determianr um atributo do objeto
        self.__limite = limite     
        
    @property
    def codigo_banco(self):
        return self.__codigo_banco
    
    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'Caixa': 104}