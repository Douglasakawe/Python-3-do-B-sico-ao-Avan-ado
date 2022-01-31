# Criar variaveis para nome (str), idade (int)
# Altura (float) e peso (float) de uma pessoa
# Criar variavel com o ano atual (int)
# Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
# Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

nome = 'Douglas Lima'
idade = 22
altura = 1.86
peso = 80
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc e {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}')