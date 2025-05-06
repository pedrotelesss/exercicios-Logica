#A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo. Calcule a conversão e construa o relatório de saída tabular (em forma de tabela de duas colunas) de graus Celsius em função de graus Fahrenheit que que variam de 45 a 80 de 1 em 1.
print("Conversor de temperaturas (F -> C)")
print("Fahreinheit | Celsius")
for grau in range (45,80+1):
    celsius = (5 / 9)*(grau - 32)
    print(f"{grau:10} | {celsius:.2f}")