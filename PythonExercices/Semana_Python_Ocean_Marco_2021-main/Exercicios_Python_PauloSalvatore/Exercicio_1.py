"""
Exercício 1
Nome: Operações Matemáticas
Objetivo: Praticar declaração de variáveis, operações matemáticas e exibição de informações no console.
Dificuldade: Principiante
1 - Declare duas variáveis numéricas 'a' e 'b' e atribua os valores 7 e 12, respectivamente;
2 - Declare uma variável chamada 'resultado' e armazene o resultado da soma entre as duas variáveis declaradas anteriormente;
3 - Exiba o resultado da soma no console;
4 - Agora declare novas linhas de exibição no console e exiba o resultado da subtração, multiplicação, divisão, exponenciação e resto da divisão inteira.
"""

# Resolução

def soma(a,b):
    valor = a + b
    return print("Soma: ", valor)

def subtracao(a,b):
    valor = a - b
    return print("Sub: ", valor)

def multiplicacao(a,b):
    valor = a * b
    return print("Mult: ", valor)

def divisao(a,b):
    valor = a / b
    return print("Div: ", valor)

def exponencial(a,b):
    valor = a ** b
    return print("Exp: ", valor)

def restodaInteira(a,b):
    valor = a % b
    return print("RestInt: ", valor)

valorA = int(input("Valor A :"))
valorB = int(input("Valor B :"))

soma(valorA,valorB)
subtracao(valorA,valorB)
multiplicacao(valorA,valorB)
divisao(valorA,valorB)
exponencial(valorA,valorB)
restodaInteira(valorA,valorB)

