def menu():
    print("|=======================|")
    print("|===== CALCULADORA =====|")
    print("| [1] ADIÇÃO            |")
    print("| [2] SUBTRAÇÃO         |")
    print("| [3] MULTIPLICAÇÃO     |")
    print("| [4] DIVISÃO           |")
    print("| [0] SAIR              |")
    print("|=======================|")
    print("Informe a opção desejada: ")


def adicao(numero_1, numero_2):
    return numero_1 + numero_2


def subtracao(numero_1, numero_2):
    return numero_1 - numero_2


def multiplicacao(numero_1, numero_2):
    return numero_1 * numero_2


def divisao(numero_1, numero_2):
    return numero_1 / numero_2


while True:
    try:
        menu()
        opcao = input("> ")
        if opcao == "1":
            primeiro_numero = float(input("Informe o 1º número: "))
            segundo_numero = float(input("Informe o 2º número: "))
            print(adicao(primeiro_numero, segundo_numero))
            input("> ")
        elif opcao == "2":
            primeiro_numero = float(input("Informe o 1º número: "))
            segundo_numero = float(input("Informe o 2º número: "))
            print(subtracao(primeiro_numero, segundo_numero))
            input("> ")
        elif opcao == "3":
            primeiro_numero = float(input("Informe o 1º número: "))
            segundo_numero = float(input("Informe o 2º número: "))
            print(multiplicacao(primeiro_numero, segundo_numero))
            input("> ")
        elif opcao == "4":
            primeiro_numero = float(input("Informe o 1º número: "))
            segundo_numero = float(input("Informe o 2º número: "))
            print(divisao(primeiro_numero, segundo_numero))
            input("> ")
        elif opcao == "0":
            print("SAINDO...")
            break
        else:
            print("Opção Inválida!")
    except:
        print("Isso não é um número!")
