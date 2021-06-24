"""
Exercício 9
Nome: Checando Múltiplos
Objetivo: Receber dois números e exibir se um é múltiplo do outro ou não.
Dificuldade: Principiante
1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Se o {numero1} for múltiplo do {numero2} exiba na tela: "O número {numero1} é múltiplo do número {numero2}.";
3 - Caso contrário, exiba na tela: "O número {numero1} não é múltiplo do número {numero2}.";
"""

# Resolução

valor = int(input("Valor1 :"))
valor2 = int(input("Valor2 :"))

if valor % valor2 == 0:
    print("Valor {} é multiplo de {}".format(valor,valor2))
else:
    print("Valor {} é não é multiplo de {}".format(valor,valor2))