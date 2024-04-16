import time

class Animal:
    def __init__(self, nome, idade, comprimento, peso, cor, especie):
        self.nome = nome
        self.idade = idade
        self.comprimento = comprimento
        self.peso = peso
        self.cor = cor
        self.especie = especie
        self.andando = False
        self.comendo = False
        self.dormindo = False
        self.emitindo_som = False

    def andar(self, destino):
        self.dormindo = False
        self.andando = True
        print(f"{self.nome}, {self.especie}, {self.cor} andou até {destino}.")
        self.loading()

    def dormir(self, lugar):
        self.andando = False
        self.comendo = False
        self.emitindo_som = False
        self.dormindo = True
        print(f"{self.nome}, {self.especie}, {self.cor} dormiu em {lugar}.")
        self.loading()

    def emitir_som(self, som):
        self.comendo = False
        self.dormindo = False
        self.andando = False
        self.emitindo_som = True
        print(f"{self.nome}, {self.especie}, {self.cor} emitiu o som '{som}'.")
        self.loading()

    def comer(self, comida):
        self.dormindo = False
        self.andando = False
        self.emitindo_som = False
        self.comendo = True
        print(f"{self.nome}, {self.especie}, {self.cor} está comendo {comida}.")
        self.loading()

    def loading(self):
        print("Carregando", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print(" Concluído!")

class Cachorro(Animal):
    def emitir_som(self):
        return "Auau!"

# Solicitar informações do usuário para criar o animal
cor_animal = input("Qual cor você quer para o animal? Diga: ")
especie_animal = input("Qual espécie você quer para o animal? Diga: ")
nome_animal = input("Qual nome você quer para o animal? Diga: ")

max = Cachorro(nome_animal, "3", "50cm", "10", cor_animal, especie_animal)
print(f"{max.nome}, {max.especie}, {max.cor} {'está' if max.andando else 'não está'} andando.")
print(f"{max.nome}, {max.especie}, {max.cor} {'está' if max.comendo else 'não está'} comendo.")
print(f"{max.nome}, {max.especie}, {max.cor} {'está' if max.dormindo else 'não está'} dormindo.")
print(f"{max.nome}, {max.especie}, {max.cor} {'está' if max.emitindo_som else 'não está'} emitindo som.")

while True:
    atividade = input("""-------------------------
    O que o animal vai fazer?
    -------------------------
    Andar (digite "Andar")
    Comer (digite "Comer")
    Dormir (digite "Dormir")
    Emitir Som (digite "Emitir Som")
    
    Nada! (digite "Nada!")
    -------------------------
    Diga aqui: """)
    
    print("")
    
    if atividade == "Andar":
        destino = input("Andar até onde? Diga: ")
        max.andar(destino)
    elif atividade == "Comer":
        comida = input("O que você quer que o animal coma? Diga: ")
        max.comer(comida)
    elif atividade == "Dormir":
        lugar = input("Dormir onde? Diga: ")
        max.dormir(lugar)
    elif atividade == "Emitir Som":
        print(max.emitir_som())
    elif atividade == "Nada!":
        break
    else:
        print("Atividade inválida.")

print("")
print("Fim do programa.")
