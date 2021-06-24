"""
Exercício 12
Nome: Praticando Funções
Objetivo: Escrever diversas funções para reaproveitar trechos de código
Dificuldade: Intermediário
Escreva um código de modo que exiba o valor do x digitado pelo usuário e que seja
substituído nas funções.
1 - Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).
2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável
de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine
o custo de produção de 100 peças.
3 - Crie uma função que receba 2 números e retorne o maior valor.
4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.
5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da
soma de f(9) + g(2). Depois crie um código que retorne o valor da soma das duas funções
com números digitados pelo usuário.
6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1.
Qual é o valor da função composta g(f(3))? Depois crie um código que retorne o valor da
soma das duas funções com números digitados pelo usuário.
7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6.
Exiba 10 números sorteados utilizando a mesma função criada.
Números aleatórios: random.randint(inicio, fim)
"""

# Resolução

import random

#Funcoes
#1
def fx(x):
    return (3 * x) - 2

#2
def custoDeProd(x):
    resultado = ( x * 2 + 30 )
    print("Custo de producao de 100 peças :", resultado)

#3
def retornaMaior(x,y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        print("{} e {} são iguais".format(x,y))

#4
def comparaValores():
    x = int(input("Numero 1:"))
    y = int(input("Numero 2:"))
    z = int(input("Numero 3:"))
    maior = retornaMaior(x,y)
    maior = retornaMaior(maior,z)
    print("Maior valor entre {} , {} , {} , é [{}]".format(x,y,z,maior))

#5
def fx5(x):
    return x - 5

def gx5(x):
    return (3 * x) + 1

def dadosEx5():
    fx = int(input("F[x]:"))
    gx = int(input("G[x]:"))
    resultado = fx5(fx) + gx5(gx)
    print("Resultado de F[{}] + G[{}] = {}".format(fx,gx,resultado))

#6
def fx6(x):
    return x - 4

def gx6(x):
    return (5 * x) + 1

def dadosEx6():
    fx = int(input("F[x]:"))
    resultado = gx6(fx6(fx))
    print("Resultado de G[F[{}] = {}".format(fx,resultado))

#7
def dado():
    for x in range(1,11): 
       resultado_dado = random.randint(1, 6)
       print("Dado {} valor : {} ".format(x,resultado_dado))

#Dados do Usuario
#1
print("\nExercicio 1")
valor_x = int(input("Valor x:"))
resultado = fx(5) + fx(0)
print("f[5]+f[0] = {}".format(resultado))

#2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável
#de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine
#o custo de produção de 100 peças.
print("\nExercicio 2")
valor_x = int(input("Numero de peças x:"))
custoDeProd(valor_x)

print("\nExercicio 3")
#3 - Crie uma função que receba 2 números e retorne o maior valor.
valor_x = int(input("Numero 1:"))
valor_y = int(input("Numero 2:"))
resultado = retornaMaior(valor_x,valor_y)
print("Maior valor :", resultado)

#4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.
print("\nExercicio 4")
comparaValores()

#5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da
#soma de f(9) + g(2). Depois crie um código que retorne o valor da soma das duas funções
#com números digitados pelo usuário.
print("\nExercicio 5")
dadosEx5()

#6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1.
#Qual é o valor da função composta g(f(3))? Depois crie um código que retorne o valor da
#soma das duas funções com números digitados pelo usuário.
print("\nExercicio 6")
dadosEx6()

#7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6.
#Exiba 10 números sorteados utilizando a mesma função criada.
#Números aleatórios: random.randint(inicio, fim)
print("\nExercicio 7")
dado()