def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

while True:
    print('Qual das funções você deseja?')
    print('1 | Imprimir de 1 a 10.')
    print('2 | Iniciar a sequência de um número de seu desejo.')
    print('3 | Sequência de números primos.')

    cod = input('Qual função você deseja: ')

    if cod == '1':
        for i in range(1, 11):
            print(i)

    elif cod == '2':
        num = int(input("Digite o número que você deseja iniciar a sequência: "))
        for i in range(num, 11):  # Ajuste aqui
            print(i)

    elif cod == '3':
        num = int(input("Digite o número máximo de números primos: "))
        for num in range(2, num + 1):
            if primo(num):
                print(num)

    else:
        print("Entrada errada, por gentileza digite '1', '2' ou '3'.")

    sec = input("Deseja continuar? (Sim/Não): ")
    if sec.lower() == 'não' or sec.lower() == 'n':
        break
    
