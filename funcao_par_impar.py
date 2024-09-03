def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    return "Impar"


valor = input("Informe um número: ")
resposta = par_impar(int(valor))
print(f"O número: {valor} é {resposta}!")
