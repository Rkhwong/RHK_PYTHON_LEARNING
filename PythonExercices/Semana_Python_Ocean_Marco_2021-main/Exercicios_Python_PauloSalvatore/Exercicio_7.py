"""
Exercício 7
Nome: Arredondando para Múltiplos
Objetivo: Receber dois números e arredondar o primeiro número para o número mais próximo do múltiplo do segundo número.
Dificuldade: Principiante
1 - Receba dois números, o primeiro na variável 'numero' e o segundo na variável 'multiplo'.
2 - Arredonde para baixo o valor do primeiro número levando em consideração que o resultado deve ser múltiplo do segundo número.
Exemplo:
Supondo que o primeiro número seja 72 e o segundo número seja 10, o resultado será 70.
Se o primeiro número for 97 e o segundo número for 10, o resultado será 90.
"""

# Resolução

valor1 = int(input("Numero : "))
valor2 = int(input("Numero Multiplo: "))

resultado = valor1 - (valor1 % valor2)

print("O valor arredondado para baixo do numero {} para que seja multiplo de {} é igual a {}.".format(valor1,valor2,resultado))
