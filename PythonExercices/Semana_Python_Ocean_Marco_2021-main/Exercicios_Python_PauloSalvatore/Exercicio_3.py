"""
Exercício 3
Nome: Input de Informações
Objetivo: Receber dados do usuário, trabalhar com os valores e exibir para o usuário.
Dificuldade: Principiante
1 - Crie um programa que receba do usuário seu nome, idade e gênero;
2 - Exiba na tela seguinte mensagem: "Olá, {nome}, você possui {idade} anos de idade e é do gênero {genero}. Já pensou no que você fará no seu aniversário de {idade + 1} anos?".
"""

def print_dados(nome,genero,idade):
    if idade > 1:
        print("Nome :", nome, "do genero", genero , "com " ,idade, "anos" )
    else:
        print("Nome :", nome, "do genero", genero , "com " ,idade, "ano" )

nome = str(input("Digite o Nome >"))
genero = str(input("\nDigite o Genero >"))
idade = int(input("\nDigite o idade >"))

print_dados(nome,genero,idade)