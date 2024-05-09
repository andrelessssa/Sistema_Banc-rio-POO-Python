from abc import ABC, abstractclassmethod,abstractproperty
from _datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(conta: Conta, transacao: Transacao):
        transacao.registro(Conta)

    def adicionar_conta(conta:Conta):
        self.contas.append(Conta)
        


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco ):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico() 

      
    @classmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo    


    @property    
    def numero(self):
        return self._numero

    @property    
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente   

    @property
    def hirtorico(self):
        return self._historico
    
    @property
    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Você não possui esse saldo disponível.")

        elif valor > 0:
            self._saldo -= valor
            print("=====Saldo Realizado=====")
            return True
        else:
            print("Operacao falhou!!! o valor informado é invalido")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso!")

        else:
            print("Operação falhou")
            return False

        return True    




class ContaCorrente(Conta):
    pass


class Historico:
    pass


class Transacao(ABC):
    pass


class Saque(Transacao):
    pass


class Deposito(Transacao):
    pass



