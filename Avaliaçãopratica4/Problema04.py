#4. Implemente o programa que gere a sequência dos números naturais na ordem crescente até um valor final fornecido (digitado) pelo usuário. Mostre também a quantidade de valores da sequência gerada.
ct = 0
inicial = int(input("Digite o número inicial da sequência:"))
final = int(input("Digite o número final da sequência:"))
for numero in range (inicial,final+1,1):
    print(numero, end=" ")
    ct +=1
print(f"\nA sequência possui {ct} números")