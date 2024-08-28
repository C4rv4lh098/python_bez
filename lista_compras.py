import os


# Função de Inserir um item
def listar():
    if len(lista_de_compras) == 0:
        print("Sem itens na lista!")
        print("="*50)
    else:
        for indice, item in enumerate(lista_de_compras):
            print(f"{indice + 1} - {item.capitalize()}")


# Função de Listar todos os itens
def adicionar():
    adicionar_item = input("Digite o nome do item: ")
    lista_de_compras.append(adicionar_item)


# Função para Apagar item pelo indice
def remover():
    if len(lista_de_compras) == 0:
        print("Sem itens na lista!")
        print("="*50)
    else:
        try:
            remover_item = input("\nDigite o indice do item: ")
            int_remover_item = int(remover_item)
            del lista_de_compras[(int_remover_item - 1)]
            limpar()
            listar()
        except ValueError:
            print("Indice inválido!")


# Função para limpar o terminal
def limpar():
    os.system("cls")


# Menu para escolha
def menu():
    print("\n|==================================|")
    print("|=========LISTA DE COMPRAS=========|")
    print("| Digite a letra da opção desejada |")
    print("| [A] - Adicionar                  |")
    print("| [R] - Remover                    |")
    print("| [L] - Listar                     |")
    print("| [S] - Sair                       |")
    print("|==================================|")


# Programa
lista_de_compras = []
while True:
    menu()
    opcao = input("| > ").lower()
    if len(opcao) > 1:
        limpar()
        print("Escreva somente uma letra!")
    elif opcao == "a":
        limpar()
        adicionar()
    elif opcao == "r":
        limpar()
        listar()
        remover()
    elif opcao == "l":
        limpar()
        listar()
    elif opcao == "s":
        print("SAINDO...")
        break
