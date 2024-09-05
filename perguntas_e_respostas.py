perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0
for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")

    opcoes = pergunta['Opcoes']
    for i, alternativa in enumerate(opcoes):
        print(f"{i+1}) {alternativa}")
    print()

    escolha = input("Selecione uma alternativa: ")

    acertou = False
    escolha_int = None
    quantidade_alternativas = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
        escolha_int -= 1

    if escolha_int is not None:
        if quantidade_alternativas > escolha_int >= 0:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        respostas_certas += 1
        print("Acertou 👍")
    else:
        print("Errou ❌")
    print()


print(f"Você acertou {respostas_certas} de {len(perguntas)} perguntas!")

