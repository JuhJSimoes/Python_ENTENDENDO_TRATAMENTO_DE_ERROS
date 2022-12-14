from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
       self.nome = nome
       self.cpf = cpf
       self.profissao = profissao
       

'''cliente = Cliente('Juh', '012.415.121-36', 'Dev II')
print(cliente.nome)
print(cliente.cpf)
print(cliente.profissao)
pprint(cliente.__dict__, width = 40)'''

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None
    
    def __init__(self, cliente, agencia, numero):
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas
        ContaCorrente.total_contas_criadas += 1
        
    def transferir(self, valor, favorecido):
        favorecido.depositar(valor, favorecido)
    
    def sacar(self, valor):
        self.saldo -= valor
        
    def depositar(self, valor):
        self.saldo += valor
        

conta_corrente = ContaCorrente(None, '00', '101')