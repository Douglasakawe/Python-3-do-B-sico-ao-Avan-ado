"""
Operadores Relacionais - AULA 10
== igualdade > maior que
>= maior que ou igual a
< Menor que
<= Menor que ou igual a
!=
"""
#var_1 = 'Roberta'
#var_2 = "Maria"
#expressao = (var_1 != var_2)
#print(expressao)

nome = input (' Qual o seu nome? ')
idade = input (' Qual a sua idade? ')

idade = int(idade)


#Limite para pegar empréstimo
idade_menor = 20 # Jovem
idade_maior = 30 # Idade máxima

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo, CONGRATS.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

