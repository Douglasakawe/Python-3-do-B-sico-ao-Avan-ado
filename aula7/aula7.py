nome = 'Douglas Akawe'
idade = 21  # int
altura = 1.86   # float
e_maior = idade > 18  # bool
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))