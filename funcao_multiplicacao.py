def multiplicacao(*args):
    resultado_multiplicacao = 1
    for numero in args:
        resultado_multiplicacao *= numero
    return resultado_multiplicacao


numeros = 1, 2, 3, 4, 5, 6
resultado = multiplicacao(*numeros)
print(resultado)