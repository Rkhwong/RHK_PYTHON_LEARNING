"""
Exercício 14
Nome: Média Escolar
Objetivo: Escrever uma aplicação utilizando funções que calcule a média de um aluno.
Dificuldade: Intermediário
1 - Um professor, muito legal, fez 3 provas durante um semestre mas só vai levar em conta as duas 
notas mais altas para calcular a média.
2 - Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, 
a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.
"""

#Tirar a Media
def mediaDasNotas(n1,n2,n3):
    return (( n1 + n2 + n3 )/3)

def mediaDasMaioresNotas ( n1, n2):
    return (( n1 + n2) / 2)

#Identifica qual a maior nota entre 2
def maiorNota(n1,n2):
    # Primeiro Maior
    if n1 > n2:
        return n1
    #Igual
    elif n1 == n2:
        return n1
    #Segundo Maior
    else:
        return n2

#Mostrar a Nota menor
def menorNota(n1,n2):
    # Segundo Maior
    if n1 < n2:
        return n1
    #Igual
    elif n1 == n2:
        return n1
    #Segundo Menor
    else:
        return n2

#Mostrar a nota mais Alta
def notasMaisAltas(notas):
    # Pegamos a maior nota entre a nota1 e a nota2
    maior1 = maiorNota(notas[0],notas[1])
    # Pegamos a maior nota entre a nota2 e a nota3
    maior2 = maiorNota(notas[1],notas[2])
    # Caso a maior nota (1) seja igual a maior nota (2), pegamos a maior nota entre a 1 e a 3
    if maior1 == maior2:
        maior2 = maiorNota(notas[0],notas[2])
    mediaMaiorNota = mediaDasMaioresNotas(maior1,maior2)
    return mediaMaiorNota

def dados():
    provas = [0,0,0]
    for x in range (3):
        provas[x] = float(input("Nota {} :".format(x+1)))
    
    mediaMaiorNota = notasMaisAltas(provas)
    # Pegamos a maior nota entre as três notas
    maior_Nota =  maiorNota(provas[0],provas[1])
    maior_Nota =  maiorNota(maior_Nota,provas[2])
    # Pegamos a menor nota entre as três notas
    menor_Nota = menorNota(provas[0],provas[1])
    menor_Nota = menorNota(menor_Nota,provas[2])
    mediaGeral = mediaDasNotas(provas[0],provas[1],provas[2])
    print("==============================\nResultados\n============================== \n    •Nota 1: {}\n    •Nota 2: {}\n    •Nota 3: {}\n    •Média Geral : {:.2f}\n    •Media das melhores Notas : {:.2f} ".format(provas[0],provas[1],provas[2],mediaGeral,mediaMaiorNota))

#Main
dados()