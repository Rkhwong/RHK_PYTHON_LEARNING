

"""# Exercício 1 - "E os 10% do garçom?"

- Defina uma variável para o valor de uma refeição que custou `R$ 42,54`;
- Defina uma variável para o valor da taxa de serviço que é de `10%`;
- Defina uma variável que calcula o valor total da conta e exiba-o no console (sem formatação, por enquanto, apenas o valor do resultado).
"""

valor_ref = float(input("Qual o Valor da ref :"))
taxa = valor_ref * 0.1
total = (valor_ref + taxa)
print(  "Valor Total :",  "{:.2f}".format(total), "\nValor Taxa :", "{:.2f}".format(taxa) )
print(  "Valor Total :",  int(total), "\nValor Taxa :", "{:.2f}".format(taxa) )