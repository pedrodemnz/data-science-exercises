aprovados = 0
reprovados = 0

while True:
    nota = input("Digite as notas dos alunos. Digite 'fim' para sair:")

    if nota.lower() == 'fim':
        break
    try:
        nota = float(nota)
        if nota >= 5:
            aprovados += 1
        else:
            reprovados += 1
    except ValueError:
        print("Digite uma nota valida ou 'fim' para sair.")

total = aprovados + reprovados

print("Resultados:")
print(f"O número de alunos que fizeram a prova: {total}")
print(f"O número de aprovados é igual a: {aprovados}")
print(f"O número de reprovados é igual a: {reprovados}")