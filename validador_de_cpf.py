import re
import sys

#"746.824.890-70"
cpf_informado = input("Informe um CPF: ")

entrada_sequencial = cpf_informado == cpf_informado[0] * len(cpf_informado)
if entrada_sequencial:
    print("Você enviou dados sequenciais!!")
    sys.exit()

cpf_informado = re.sub(r'[^0-9]', "", cpf_informado)
resultado_soma_digitos_1 = 0
contador_regressivo_1 = 10
nove_digitos = cpf_informado[:9]
for digito in nove_digitos:
    resultado_soma_digitos_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
primeiro_digito = (resultado_soma_digitos_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

resultado_soma_digitos_2 = 0
contador_regressivo_2 = 11
dez_digitos = nove_digitos + str(primeiro_digito)
for digito in dez_digitos:
    resultado_soma_digitos_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
segundo_digito = (resultado_soma_digitos_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f"{nove_digitos}{primeiro_digito}{segundo_digito}"

if cpf_informado == cpf_gerado:
    # print(f"CPF: '{cpf_gerado}' é válido!")
    print(f"CPF: '{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}"
          f"-{primeiro_digito}{segundo_digito}'é válido!")
else:
    print("CPF inválido!")
