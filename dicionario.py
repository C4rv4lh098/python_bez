pessoa = {
    'nome': "Rodrigo Moura",
    'sobrenome': "Carvalho",
    # 'idade': 26,
}
print(pessoa.get('nome', 'Não existe'))
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))


pessoa.setdefault('idade', 0)
print(pessoa['idade'])
for valor in pessoa.values():
    print(valor)


for chave, valor in pessoa.items():
    print(chave, valor)

nome = pessoa.pop('nome')  # Remove a chave especificada do dicionário
ultima_chave = pessoa.popitem()  # Remove a última chave do dicionário

pessoa.update({
    # Atualiza com as informações passadas por aqui
    'nome': "Novo nome",
    'idade': 26,  # Nova chave
})
