from selectors import SelectSelector

som_par = 0
qtd_par = 0
som_impar = 0
qtd_impar = 0

while True:
    numero = int(input("Digite um número. Digite '0' para sair."))

    if numero == 0:
        break

    if numero % 2 == 0:
        som_par += numero
        qtd_par += 1
    else:
        som_impar += numero
        qtd_impar += +1

med_par = som_par / qtd_par if qtd_par > 0 else 0
med_impar = som_impar / qtd_impar if qtd_impar > 0 else 0

print(f"Média dos pares é igual a: {med_par}")
print(f"Média dos impares é igual a: {med_impar}")