class Cbancaria:
    def __init__(self, titular, saldo, limite, numeroCont):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.numeroCont = numeroCont
        self.ativa = True

    def sacar(self, valor):
        if self.ativa:
            if self.saldo - valor >= -self.limite:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta bloqueada. Não é possível sacar.")

    def depositar(self, valor):
        if self.ativa:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Conta bloqueada. Não é possível depositar.")

    def bloqueCont(self):
        self.ativa = False
        print("Conta bloqueada.")

    def desbloCont(self):
        self.ativa = True
        print("Conta desbloqueada.")

    def veriSaldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def mudarLimi(self, nLimite):
        if self.ativa:
            self.limite = nLimite
            print(f"Limite alterado para R${nLimite:.2f}.")
        else:
            print("Conta bloqueada. Não é possível alterar o limite.")

# Exemplo de uso da classe ContaBancaria
minhaConta = Cbancaria("João", 5000.0, 2000.0, "1234-5")

titular = input("Informe o titular da conta: ")
saldo = float(input("Informe o saldo inicial da conta: "))
limite = float(input("Informe o limite da conta: "))
numero_conta = input("Informe o número da conta: ")

minhaConta = Cbancaria(titular, saldo, limite, numero_conta)

print("Saldo inicial:")
minhaConta.veriSaldo()

print("")

valorDep = float(input("Informe o valor que deseja depositar: "))
minhaConta.depositar(valorDep)

valorSaque = float(input("Informe o valor que deseja sacar: "))
minhaConta.sacar(valorSaque)

print("Saldo após depósito e saque:")
minhaConta.veriSaldo()

bloqConta = input("Deseja bloquear a conta? (sim/não): ")
if bloqConta.lower() == "sim":
    minhaConta.bloqueCont()
else:
    minhaConta.desbloCont()

novLimite = float(input("Informe o novo limite da conta: "))
minhaConta.mudarLimi(novLimite)