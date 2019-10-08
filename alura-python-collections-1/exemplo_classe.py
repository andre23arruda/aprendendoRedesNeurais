#%%
class ContaCorrente:

    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return f'>> Codigo: {self.codigo} \n>> Saldo {self.saldo}'

#%%
conta_do_andre = ContaCorrente(15)
print(conta_do_andre)

#%%
conta_do_andre.deposita(1000)
print(conta_do_andre)

#%%
class ContaSalario:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposit(self,valor):
        self._saldo += valor

    def __str__(self):
        return f'>> Codigo: {self._codigo} \n>> Saldo {self._saldo}'
#%%
conta1 = ContaSalario(37)
print(conta1)
conta2 = ContaSalario(37)
print(conta2)
conta1 == conta2

#%%
class ContaSalario:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposit(self,valor):
        self._saldo += valor

    def __eq__(self,outro):
        return self._codigo == outro._codigo

    def __str__(self):
        return f'>> Codigo: {self._codigo} \n>> Saldo {self._saldo}'

