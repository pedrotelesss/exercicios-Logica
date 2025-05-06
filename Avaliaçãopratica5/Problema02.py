#Melhore o programa anterior para torná-lo mais abrangente. Agora, o usuário fornecerá os valores inicial e final de graus Fahrenheit. Calcule a conversão e gere o relatório de saída tabular (em forma de tabela) considerando o intervalo digitado. Gere o relatório na ordem crescente, se o valor inicial for menor ou igual ao valor final. E na ordem decrescente, se valor inicial for maior que o valor final.
print("Conversor de temperaturas (F -> C)")
f_inicio = int(input("Digite o inicio da variação:"))
f_final = int(input("Digite o final da variação:"))
if f_inicio<f_final:
    print("Fahreinheit | Celsius")
    for grau in range (f_inicio,f_final+1):
        celsius = (5 / 9)*(grau - 32)
        print(f"{grau:10} | {celsius:.2f}")
else:
    print("Fahreinheit | Celsius")
    for grau in range(f_inicio, f_final - 1,-1):
        celsius = (5 / 9) * (grau - 32)
        print(f"{grau:10} | {celsius:.2f}")