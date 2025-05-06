#Vamos tornar o programa anterior mais interessante. Agora, o programa deve gerar a tabuada de multiplicação de um número inteiro qualquer fornecido pelo usuário.
print("Tabuada")
n1 = int(input("Digite o número para ser multiplicado:"))
for numero in range (0,10+1):
    resultado = numero*n1
    print(f"{n1}X{numero} = {resultado}")