from abc import ABC, abstractclassmethod,abstractproperty
import textwrap
from _datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self, conta, transacao):
        transacao.registro(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)
        


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
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.hirtorico.transacoes if transacao["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques


        if excedeu_limite:
            print("\n Operacao falhou!! O valor do saque excedeu ")
        elif excedeu_saques:
            print("operacao falhou! numero de saques excedido")

        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"""\
            Agência: \t{self.agencia}
            C/C: \t\t{self.numero}
            Título: \t{self.cliente.nome}
            """
          

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacoes(self, transacao):
        self._transacoes.append(
        {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%y %H:%M:%S"),
        }
    )   
    

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)    


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)    




def menu():

    menu = """\n
    ================= MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

"""
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if