#Desenvolva o programa que calcule a média aritmética de uma turma, onde cada aluno realizou uma avaliação. Não sabemos a quantidade de alunos, por isso usaremos o valor “-1” como condição (flag) de saída. Na tela de saída, mostre a média aritmética da turma e a quantidade de alunos da turma
desempenho = []
print("Digite o número [-1] para encerrar o loop")
while True:
    notas = int(input("Digite a nota do aluno:"))
    if notas == -1:
        break
    desempenho.append(notas)
print(f"Quantidade de alunos: {len(desempenho)}")
print(f"Média das notas: {sum(desempenho)/len(desempenho)}")