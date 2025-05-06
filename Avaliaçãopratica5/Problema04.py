#Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.
soma_m3 = 0
soma_impar = 0
for n in range (0,500,3):
    soma_m3 += n
for impar in range (1,500,2):
    soma_impar += impar
soma_total = soma_impar + soma_m3
print(f"A soma de todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três é igual a {soma_total}")