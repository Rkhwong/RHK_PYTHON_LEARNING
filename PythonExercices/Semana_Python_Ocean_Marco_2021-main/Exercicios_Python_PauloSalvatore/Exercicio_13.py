"""
Exercício 13
Nome: Convertendo Celsius/Farenheit
Objetivo: Escrever duas funções de conversão, uma de graus celsius em farenheit e a outra que faça o contrário.
Dificuldade: Principiante
1 - Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit.
2 - Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão escolhida é realizada.
3 - Se C é a temperatura em Celsius e F em farenheit, as fórmulas de conversão são:
C = 5 * (F - 32) / 9
F = (9 * C / 5) + 32
"""

def converterCF(c):
    f = (( 9 * c )/ 5 ) + 32
    print("Valor Convertido em Fº {:.2f}".format(f))

def converterFC(f):
    c = 5 * ( f - 32) / 9
    print("Valor Convertido em Cº {:.2f}".format(c))

def dadosUsuario():
    escolha = int(input("Escolha o Tipo de Temperatura\n    [1]Celcius\n    [2]Farenheit\nEscolha :"))
    if escolha == 1:
        valorCelsius = float(input("Valor da temperatura Cº :"))
        converterCF(valorCelsius)
    elif escolha == 2:
        valorFarenheit = float(input("Valor da temperatura Fº :"))
        converterFC(valorFarenheit)
    else:
        print("Escolha Invalida!")

#Main
dadosUsuario()
