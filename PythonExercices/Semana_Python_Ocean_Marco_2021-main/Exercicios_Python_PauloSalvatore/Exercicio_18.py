"""
Exercício 18
Nome: Praticando: Funções Matemáticas
Objetivo: Escrever diversas funções que utilizem as funções matemáticas como base para trabalhar com números 
e praticar a formatação de números e strings.

Dificuldade: Principiante
1 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_maior_valor' 
utilizando o método '*args' e retorne o maior deles utilizando a função max()

2 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_menor_valor' 
utilizando o método '*args' e retorne o menor deles utilizando a função min()

3 - Peça para o usuário digitar 3 números positivos e 3 números negativos, extraia o módulo (versão positiva) 
de cada número utilizando a função abs() e exiba na tela o maior e o menor número 
(utilize as funções criadas anteriormente no exercício 1 e 2).

4 - Declare uma função que recebe um número e o formata de acordo com o tipo de sua variável (utilize a função type())
- Se a variável for um float, formate-a como moeda, exemplo:

- Entra a variável float 20.0 e exibe na tela R$ 20,00. Regra de formatação: {:.2f}, onde 2 representa o número e casas decimais.

- Se a variável for um int, formate-a deixando com pelo menos 5 dígitos (colocando zeros na frente). 
Regra de formatação: {:02d}, onde 2 representa o número de dígitos.

- Se a variável for uma string, formata-a para que utilize 10 espaços adicionais à esquerda. 
Regra de formatação: {:>1}, onde 1 representa o número de espaços que irá utilizar.

- Caso a variável não seja nenhuma dessas, exiba a mensagem "Esse tipo de variável não está mapeado."
"""

#Recebe Numeros do Usuario
def novoNumero():
    novoNum =  float(input(" Digite um Numero : "))
    return novoNum

def novoNumeroPos():
    novoNum =  float(input(" Digite um Numero Positivo : "))
    return novoNum

def novoNumeroNeg():
    novoNum =  float(input(" Digite um Numero Negativo : "))
    return novoNum

def novoInt():
    novoNum =  int(input(" Digite um Numero : "))
    return novoNum

def novoFloat():
    novoNum =  float(input(" Digite um Float : "))
    return novoNum

def novaStr():
    novoNum =  str(input(" Digite um Str : "))
    return novoNum
#2
def pegar_maior_valor(*num):
    return max(num)

#3
def pegar_menor_valor(*num):
    return min(num)

def tipoVariavel(var):
    tipo = type(var)
    if tipo == int:
        print("Variavel formatada : {:02d}".format(var))
    elif tipo == float:
        print("Variavel formatada : {:.2f}".format(var))
    elif tipo == str:
        print("Variavel formatada : {:>10}".format(var))
    else:
        print("Variavel fora do padrao de formatacao")

def main():
    #Dados Usuario
    num1 = novoNumero()
    num2 = novoNumero()
    num3 = novoNumero()

    maiorValor = pegar_maior_valor(num1,num2,num3)
    menorValor = pegar_menor_valor(num1,num2,num3)
    print("    1 - Maior Valor : {}\n    2 - Menor Valor : {}".format(maiorValor,menorValor))

    print("\nExercicio 2:")
    #Dados Usuario
    numPos1 = novoNumeroPos()
    numPos2 = novoNumeroPos()
    numPos3 = novoNumeroPos()
    numNeg1 = novoNumeroNeg()
    numNeg2 = novoNumeroNeg()
    numNeg3 = novoNumeroNeg()
    #Funcao Abs Transforma Negativo
    new_numNeg1 = abs(numNeg1)
    new_numNeg2 = abs(numNeg2)
    new_numNeg3 = abs(numNeg3)

    maiorValor = pegar_maior_valor(numPos1,numPos2,numPos3,new_numNeg1,new_numNeg2,new_numNeg3)
    menorValor = pegar_menor_valor(numPos1,numPos2,numPos3,new_numNeg1,new_numNeg2,new_numNeg3)
    print("    1 - Maior Valor : {}\n    2 - Menor Valor : {}".format(maiorValor,menorValor))

    print("\nExercicio 3:")
    novo_Int = novoInt()
    novo_Float = novoFloat()
    novo_Str = novaStr()
    
    tipoVariavel(novo_Int)
    tipoVariavel(novo_Float)
    tipoVariavel(novo_Str)
    
main()