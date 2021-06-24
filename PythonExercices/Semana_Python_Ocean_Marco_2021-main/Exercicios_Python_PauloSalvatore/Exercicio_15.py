"""
Exercício 15
Nome: Gastos da Viagem
Objetivo: Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.
Dificuldade: Intermediário
Hospedagem
1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.
Passagem
2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
- São Paulo custa R$ 312,00;
- Porto Alegre custa R$ 447,00;
- Recife custa R$ 831,00;
- Manaus custa R$ 986,00.
Aluguel de Carro
3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
- Calcule o custo do aluguel do carro sendo que:
- A cada dia o carro custa R$ 40,00;
- Alugando 7 dias ou +: R$ 50,00 de desconto;
- Alugando 3 dias ou +: R$ 20,00 de desconto;
- Você pode receber apenas um desconto;
- Retorne o custo.
Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!
Gastos Extras
5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.
"""

#Imprime Os Dados
def imprimeCustos(hotel,custocidade,carro,dias,lugar):
    custoTotal = hotel+custocidade+carro
    print("Custos\n    Custo Total :{}\n    •Hotel:{}\n    •Cidade {}:R${}\n    •Aluguel do Carro:R${} por {} dias".format(custoTotal,hotel, lugar,custocidade,carro,dias))


def Main():
    print("Dados do Usuario")
    #Hotel
    noites = int(input("Digite quantas Noites vai pernoitar : "))
    custoHotel = custo_hotel(noites)
    #Cidade
    cidade = int(input("Digite para qual cidade voce vai ?\n    [1] São Paulo\n    [2] Porto Alegre\n    [3] Recife\n    [4] Manaus\n   Escolha>"))
    if cidade < 1 or cidade > 4:
        print("Escolha Invalida !")
    else:
        custoAviao = custo_aviao(cidade)
    #Carro
    dias = int(input("Digite quantos Dias vai alugar o carro : "))
    custoCarro = custo_carro(dias)
    lugar = cidadeEscolhida(cidade)
    imprimeCustos( custoHotel, custoAviao, custoCarro, dias, lugar)
    
#funções
#1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' 
# e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.

#Hospedagem
def custo_hotel(noites):
    return (noites * 140)
    #print("Custo Total de Hotel :", custoTotalHotel)

def cidadeEscolhida(cidade):
    cidadeTable = [["São Paulo","Porto Alegre","Recife","Manaus"],[312,447,831,986]]
    return cidadeTable[0][cidade-1]
#Passagem

def custo_aviao(cidade):
    cidadeTable = [["São Paulo","Porto Alegre","Recife","Manaus"],[312,447,831,986]]
    return cidadeTable[1][cidade-1]
    #print("Valor da Passagem : {:.2f}".format(cidadeTable[1][cidade-1]))

#Aluguel de Carro
def custo_carro(dias):
    if dias >= 7:
        return (dias * 40) - 50
    elif dias >= 3 and dias < 7:
        return (dias * 40) - 20
    elif dias <= 2:
        return dias * 40
    elif dias < 0:
        print("Dias Invalidos!")
        return False
        

#main
Main()
