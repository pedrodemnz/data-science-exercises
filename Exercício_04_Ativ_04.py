soma = 0

for n in range(1, 500):
    if n % 2 != 0 and n % 3 == 0:
        soma += n
print(soma)