#5. Implemente o programa que gere a sequência dos números naturais na ordem decrescente até o valor zero e o valor inicial será fornecido (digitado) pelo usuário. Mostre também a quantidade de valores da sequência gerada.
ct = 0
inicial = int(input("Digite o número inicial da sequência:"))
for n in range (inicial,0-1,-1):
    print(n, end=" ")
    ct+=1
print(f"\nA sequência possui {ct} números")