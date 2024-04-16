

rotina = True

class Pessoa:
   def __init__(self, altura, idade, nome, peso, genero):
       self.andando = False
       self.comendo = False
       self.dormindo = False
       self.falando = False
       self.altura = altura
       self.idade = idade
       self.nome = nome
       self.peso = peso
       self.genero = genero

   def andar(self, destino):
       self.dormindo = False
       self.andando = True
       print(f"{self.nome} está andando até {destino}.")

   def andar_parar(self):
       if self.andando:
           self.andando = False
           print(f"{self.nome} parou de andar.")

   def comer(self, alimento):
       self.comendo = True
       self.dormindo = False
       self.falando = False
       print(f"{self.nome} está comendo {alimento}.")

   def comer_parar(self):
       if self.comendo:
           self.comendo = False
           print(f"{self.nome} parou de comer.")

   def dormir(self, onde):
       self.andando = False
       self.dormindo = True
       self.comendo = False
       self.falando = False
       print(f"{self.nome} está dormindo em {onde}.")

   def dormir_parar(self):
       if self.dormindo:
           self.dormindo = False
           print(f"{self.nome} parou de dormir.")

   def falar(self, fala):
       self.comendo = False
       self.dormindo = False
       self.falando = True
       print(f"{self.nome} está falando: '{fala}'.")

   def falar_parar(self):
       if self.falando:
           self.falando = False
           print(f"{self.nome} parou de falar.")

def minharotina(pessoa):
   while rotina:
       print(f"{pessoa.nome} {'está' if pessoa.andando else 'não está'} andando.")
       print(f"{pessoa.nome} {'está' if pessoa.comendo else 'não está'} comendo.")
       print(f"{pessoa.nome} {'está' if pessoa.dormindo else 'não está'} dormindo.")
       print(f"{pessoa.nome} {'está' if pessoa.falando else 'não está'} falando.")
       atividadea = input("""
O que a pessoa vai fazer?
          ...          
Andar    (digite "Andar")
Comer    (digite "Comer")
Dormir  (digite "Dormir")
Falar    (digite "Falar")
          ...          
Nada!    (digite "Nada!")


Diga: """)
       if atividadea == "Andar":
           if pessoa.dormindo:
               print(f"{pessoa.nome} está dormindo, deseja que ele(a) pare?")
               atividadeb = input("Diga 'Sim' ou 'Não': ")
               if atividadeb == "Sim":
                   pessoa.dormir_parar()
                   atividadec = input("Andar até onde? Diga: ")
                   pessoa.andar(atividadec)
               elif atividadeb == "Não":
                   print(f"{pessoa.nome} segue fazendo o que estava.")
               else:
                   print("Atividade inválida!")
           else:
               atividadeb = input("Andar até onde? Diga: ")
               pessoa.andar(atividadeb)
       elif atividadea == "Comer":
           if pessoa.dormindo or pessoa.falando:
               print(f"{pessoa.nome} está dormindo ou falando, deseja que ele(a) pare?")
               atividadeb = input("Diga 'Sim' ou 'Não': ")
               if atividadeb == "Sim":
                   pessoa.dormir_parar()
                   pessoa.falar_parar()
                   atividadec = input("Comer o quê? Diga: ")
                   pessoa.comer(atividadec)
               elif atividadeb == "Não":
                   print(f"{pessoa.nome} segue fazendo o que estava.")
               else:
                   print("Atividade inválida!")
           else:
               atividadeb = input("Comer o quê? Diga: ")
               pessoa.comer(atividadeb)
       elif atividadea == "Dormir":
           if pessoa.andando or pessoa.comendo or pessoa.falando:
               print(f"{pessoa.nome} está andando, comendo ou falando, deseja que ele(a) pare?")
               atividadeb = input("Diga 'Sim' ou 'Não: ")
               if atividadeb == "Sim":
                   pessoa.andar_parar()
                   pessoa.comer_parar()
                   pessoa.falar_parar()
                   atividadec = input("Dormir onde? Diga: ")
                   pessoa.dormir(atividadec)
               elif atividadeb == "Não":
                   print(f"{pessoa.nome} segue fazendo o que estava.")
               else:
                   print("Atividade inválida!")
           else:
               atividadeb = input("Dormir onde? Diga: ")
               pessoa.dormir(atividadeb)
       elif atividadea == "Falar":
           if pessoa.comendo or pessoa.dormindo:
               print(f"{pessoa.nome} está comendo ou dormindo, deseja que ele(a) pare?")
               atividadeb = input("Diga 'Sim' ou 'Não: ")
               if atividadeb == "Sim":
                   pessoa.comer_parar()
                   pessoa.dormir_parar()
                   atividadec = input("Falar o quê? Diga:")
                   pessoa.falar(atividadec)
               elif atividadeb == "Não":
                   print(f"{pessoa.nome} segue fazendo o que estava.")
               else:
                   print("Atividade inválida!")
           else:
               atividadeb = input("Falar o quê? Diga: ")
               pessoa.andar(atividadeb)
       elif atividadea == "Nada!":
           break
       else:
           print("Atividade inválida!")
       print("")
   print("Este é o fim do programa.")

Miguel = Pessoa("1,85", "17", "Miguel", "92", "Masculino")
Mateo = Pessoa("1,85", "16", "Mateo", "71", "Masculino")
atividade = input("""Bem vindo ao Minha Rotina


Quem você quer ser?
          ...          
Miguel      (digite Miguel)
Mateo      (digite Mateo)
Diga: """)
print("")
if atividade == "Miguel":
   minharotina(Miguel)
elif atividade == "Mateo":
   minharotina(Mateo)
else:
   print("Pessoa inválida!")

