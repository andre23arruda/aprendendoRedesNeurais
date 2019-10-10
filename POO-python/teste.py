#%% Importando classe conta
from conta import Conta

#%% Criando conta
conta1 = Conta(123,'André',10,1000)

#%% Atributo saldo
conta1.saldo # exibe atributo saldo

#%% Métodos do objeto conta
conta1.extrato()
conta1.deposita(10)
conta1.saca(30)

#%% Ponteiros de variaveis em python
conta2 = conta1 # aponta para conta1
conta2 = None # não aponta para nada

#%% Atributos normais e privados
print(f'{conta1._Conta__limite}') # acessando atributo privado (não é bom fazer isso)
# é melhor criar um método para acessar o atributo e modificar
print(f'{conta1.saldo}') # acessando atributo privado

#%% Método de tranferencia entre contas
conta2 = Conta(1234,'Joao',100,1000)
conta2.transfere(50,conta1)
conta2.extrato()

#%% Método de verificação de inadimplencia
conta2.eh_inadimplente()
conta2.saca(3000)
conta2.eh_inadimplente()

#%% get e set
print(conta1.get_saldo())
conta1.set_limite(5000)
print(conta1._Conta__limite)


#%% Importando classe cliente
# @property e @setter
from cliente import Cliente

cliente1 = Cliente('andré', 24)
cliente1.nome

cliente2 = Cliente('joao', 29)
print(cliente2.idade)
cliente2.idade = 25
print(cliente2.idade)


#%% Explorando os métodos da classe conta
from conta import Conta
conta1 = Conta(123,'André',10,1000)
conta1.saca(10030)

#%% Explorando os métodos da classe conta (parte 2)
from conta import Conta
conta1 = Conta(123,'André',10,1000)
print(conta1.codigo_banco)
print(conta1.codigo_bancos()) # método estático, bom para fazer função que não envolve o objeto






