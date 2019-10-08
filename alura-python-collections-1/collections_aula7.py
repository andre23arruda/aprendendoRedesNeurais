#%%
class ContaSalario:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposit(self,valor):
        self._saldo += valor

    def __lt__(self,outro): # less than (comparação entre objetos de acordo com um atributo)
        return self._saldo < outro._saldo

    def __eq__(self,outro): # equal (comparação de igualdade entre objetos de acordo com um atributo)
        return self._codigo == outro._codigo

    def __str__(self):
        return f'>> Codigo: {self._codigo} \n>> Saldo {self._saldo}'

#%%
conta_do_andre = ContaSalario(1)
conta_do_andre.deposit(100)
conta_do_joao = ContaSalario(2)
conta_do_joao.deposit(200)
conta_do_joao > conta_do_andre

#%%
list_contas = [conta_do_andre,conta_do_joao]
for conta in sorted(list_contas):
    print(conta)