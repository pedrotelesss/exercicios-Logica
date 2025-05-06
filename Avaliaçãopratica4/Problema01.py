#1. Elabore o programa que gere a sequência dos números naturais ímpares até 13. Mostre também a quantidade de números da sequência gerados, use contador.
ct = 0
for numero in range (1,13+1,2):
    ct +=1
    print(numero, end=" ")
print(f"\nForam gerados {ct} números")