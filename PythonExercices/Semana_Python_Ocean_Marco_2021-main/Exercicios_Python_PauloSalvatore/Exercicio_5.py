"""
Exercício 5
Nome: Par ou Ímpar
Objetivo: Receber um número do usuário e informar se ele é par ou ímpar.
Dificuldade: Principiante
1 - Crie um programa que receba do usuário um número;
2 - Caso o número seja par, exibir a mensagem no console "O número {numero} é par.";
3 - Caso contrário, exibir a mensagem "O número {numero} é ímpar.".
"""
"""
# Resolução

numero = int(input("Insira um número: "))

if numero % 2 == 0:
	print("O número {} é par.".format(numero))
else:
	print("O número {} é ímpar.".format(numero))
"""
def calculo(valor):
    valor = valor % 2
    if valor != 0:
        print("Numero eh Impar!")
    else:
        print("Numero eh Par!")

valor = int(input("Digite um Numero >"))

calculo(valor)