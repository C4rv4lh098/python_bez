import os

palavra_secreta = "perfume"
letras_acertada = ""
numero_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ").lower()
    numero_tentativas += 1

    if letra_digitada == "sair":
        print("SAINDO...")
        break

    if len(letra_digitada) > 1:
        print("Digite somente uma letra!")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertada += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(f"Palavra formada: {palavra_formada}")

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("VOCÊ GANHOU!!!!!")
        print(f"A palavra era: '{palavra_formada.upper()}'")
        print(f"Você conseguiu com {numero_tentativas} tentativas!")
        letras_acertada = ""
        numero_tentativas = 0
