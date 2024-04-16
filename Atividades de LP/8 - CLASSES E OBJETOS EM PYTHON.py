
"""Atividade 1"""

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print("Endereço:", self.endereco)

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

pessoa1 = Pessoa("João", 25, "Rua A, 123")
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
pessoa1.mostrar_endereco()
pessoa1.alterar_endereco("Rua B, 456")
pessoa1.mostrar_endereco()

"""Atividade 2"""

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        print("Curso:", self.curso)

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso


aluno1 = Aluno("Maria", 12345, "Engenharia")
print("Nome:", aluno1.nome)
print("Matrícula:", aluno1.matricula)
aluno1.mostrar_curso()
aluno1.alterar_curso("Medicina")
aluno1.mostrar_curso()

"""Atividade 3"""

class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

88
alunos = []
for i in range(5):
    matricula = int(input("Digite a matrícula do aluno {}: ".format(i + 1)))
    nome = input("Digite o nome do aluno {}: ".format(i + 1))
    nota1 = float(input("Digite a nota da primeira prova do aluno {}: ".format(i + 1)))
    nota2 = float(input("Digite a nota da segunda prova do aluno {}: ".format(i + 1)))
    nota3 = float(input("Digite a nota da terceira prova do aluno {}: ".format(i + 1)))
    aluno = Aluno(matricula, nome, nota1, nota2, nota3)
    alunos.append(aluno)

maior_media = 0
aluno_maior_media = None
for aluno in alunos:
    media = aluno.calcular_media()
    if media > maior_media:
        maior_media = media
        aluno_maior_media = aluno

print("Aluno com maior média geral:", aluno_maior_media.nome)

menor_media = float('inf')
aluno_menor_media = None
for aluno in alunos:
    media = aluno.calcular_media()
    if media < menor_media:
        menor_media = media
        aluno_menor_media = aluno

print("Aluno com menor média geral:", aluno_menor_media.nome)

for aluno in alunos:
    if aluno.calcular_media() >= 6:
        print(aluno.nome, "foi aprovado.")
    else:
        print(aluno.nome, "foi reprovado.")

"""Atividade 4"""

class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo + segundos
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60

    def diferenca_horarios(self, outro_horario):
        total_segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        diferenca = abs(total_segundos_atual - total_segundos_outro)
        diferenca_horas = diferenca // 3600
        diferenca_minutos = (diferenca % 3600) // 60
        diferenca_segundos = diferenca % 60
        return diferenca_horas, diferenca_minutos, diferenca_segundos


horario1 = Horario(10, 30, 45)
horario2 = Horario(8, 15, 20)
horario1.incrementar_segundos(1000)
print("Horário 1:", horario1.hora, "h", horario1.minuto, "min", horario1.segundo, "s")
diferenca = horario1.diferenca_horarios(horario2)
print("Diferença entre horário 1 e horário 2:", diferenca[0], "h", diferenca[1], "min", diferenca[2], "s")

"""Atividade 5"""

class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        print("Preço:", self.preco)

    def exibir_dados(self):
        print("Marca:", self.marca)
        print("Ano:", self.ano)
        self.mostrar_preco()


carro1 = Carro("Toyota", 2020, 50000)
carro1.exibir_dados()

"""Atividade 6"""

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        if self.fome <= 50 and self.saude >= 50:
            return "Feliz"
        else:
            return "Triste"


tamagushi1 = Tamagushi("Tama", 30, 60, 2)
print("Nome:", tamagushi1.retornar_nome())
print("Fome:", tamagushi1.retornar_fome())
print("Saúde:", tamagushi1.retornar_saude())
print("Idade:", tamagushi1.retornar_idade())
print("Humor:", tamagushi1.calcular_humor())

"""Atividade 7"""

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        if isinstance(alimento, Macaco):
            alimento.digerir()
            print(self.nome, "comeu", alimento.nome)
        else:
            self.bucho.append(alimento)

    def ver_bucho(self):
        print("Bucho do", self.nome + ":", self.bucho)

    def digerir(self):
        if self.bucho:
            comida = self.bucho.pop(0)
            print(self.nome, "digeriu", comida)
        else:
            print("Bucho do", self.nome, "está vazio.")



macaco1 = Macaco("Jorge")
macaco2 = Macaco("Ana")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Pêssego")

macaco2.comer("Nozes")
macaco2.comer("Uvas")
macaco2.comer("Cenoura")

macaco1.ver_bucho()
macaco1.comer(macaco2)
macaco1.ver_bucho()
macaco1.digerir()
macaco1.ver_bucho()