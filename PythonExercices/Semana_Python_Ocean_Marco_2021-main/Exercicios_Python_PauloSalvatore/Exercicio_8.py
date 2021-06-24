"""
Exercício 8
Nome: Comparação de Números: Maior, Menor ou Igual
Objetivo: Receber dois números e exibir qual é maior, menor ou igual a quem.
Dificuldade: Principiante
1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Caso o {numero1} seja maior do que o {numero2}, exiba na tela: "O número {numero1} é maior do que o número {numero2}.";
3 - Caso contrário, se o {numero1} for menor, exiba: "O número {numero1} é menor que {numero2}.";
4 - Caso contrário, exiba: "O número {numero1} é igual ao número {numero2}.".
"""

# Resolução

def compararNum(x,y):
    if x > y:
        print("{} Maior que {}".format(x,y))
    elif x < y:
        print("{} Menor que {}".format(x,y))
    else:
        print("{} Igual que {}".format(x,y))


x = int(input("Valor A:"))
y = int(input("Valor B:"))
compararNum(x,y)