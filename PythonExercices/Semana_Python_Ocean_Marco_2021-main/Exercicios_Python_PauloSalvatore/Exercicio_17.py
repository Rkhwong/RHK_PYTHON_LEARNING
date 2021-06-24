"""
Exercício 17
Nome: Par ou Ímpar: Funções
Objetivo: Escrever uma função chamada numero_par que recebe um número e torna True caso ele seja par ou False caso seja ímpar
Dificuldade: Principiante
1 - Crie uma função chamada 'numero_par(numero)' que receba um número como argumento e retorne True caso ele seja par ou False caso seja ímpar.
2 - O número checado deve ser digitado pelo usuário.
"""

def numero_par(num):
    # num mod de 2 for igual a 0
    if num % 2 == 0:
        #Par
        print("Par")
        return True
    else:
        #Impar
        print("Impar")
        return False

numero = int(input("Numero ? >"))

resultado = numero_par(numero)
print(resultado)