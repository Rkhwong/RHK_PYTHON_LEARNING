"""
Exercício 19
Nome: Praticando: Listas/For (Loop)
Objetivo: Praticar a criação e a leitura básica de listas com números e textos.
Dificuldade: Intermediário
1 - Crie uma lista com alguns números inseridos manualmente (não há necessidade do usuário inserí-los).
2 - Crie um for que varra cada elemento da lista e exiba-o no console.
3 - Declare um novo for que exiba apenas os números maiores que 3.
4 - Declare um outro for que exiba apenas os números pares.
5 - Exiba na tela a soma de todos os elementos da lista sem a utilização de funções extras.
6 - Exiba a soma de todos os elementos utilizando a função sum().
7 - Crie uma nova lista a partir de números digitados pelo usuário, faça com que o usuário insira 10 números, porém, 
utilize o 'for' para isso, em vez de declarar 10 vezes o input de entrada de informação, declare apenas UMA vez e faça com que ele seja executado 10 vezes.
A cada atualização da lista, exiba a quantidade de elementos que ela possui.
8 - Exiba apenas os três primeiros elementos da lista no console.
9 - Exiba apenas os três últimos elementos da lista no console.
10 - Declare uma nova lista vazia chamada 'nomes' e armazene 3 nomes digitados pelo usuário, 
ordene esses nomes por ordem alfabética e exiba-os na tela, um de cada vez.
"""

print("\nItem 1")
lista = [1,2,3,4,5,6,7,8,9,10]

print("\nItem 2")
for x in lista:
    print(lista[x-1])

print("\nItem 3")
for x in lista:
    if x > 3:
        print(lista[x-1])
print("\nItem 4")
for x in lista:
    if x % 2 == 0:
        print(lista[x-1])

print("\nItem 5")
total = 0
for x in lista:
    total += lista[x-1]
print("Total = ",total)

print("\nItem 6")
total = sum(lista)
print("Soma Total : ",total)

print("\nItem 7")
novaLista = []
for x in range(10):
    novoNumero = int(input("Digite um numero:"))
    novaLista.append(novoNumero)
    print("A lista possui {} elementos ".format(len(novaLista)))
print(novaLista)

print("\nItem 8")
print("Os 3 primeiros dados são {}".format(novaLista[:3]))

print("\nItem 9")
print("Os 3 ultimos dados são {}".format(novaLista[7:10]))
print("Os 3 ultimos dados são {}".format(novaLista[len(novaLista)-3:len(novaLista)]))

print("\nItem 10")

lista_nomes = []
for x in range(3):
    nome = input("Digite o {}º nome ".format(x + 1))
    lista_nomes.append(nome)

# sort() Ordena
lista_nomes.sort()

for nome in lista_nomes:
    print(nome)