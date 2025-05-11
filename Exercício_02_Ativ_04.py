vi = int(input("Digite o valor inicial: "))
vf = int(input("Digite o valor final: "))

for n in range(vi, vf + 1, 1):
    print(f"{n} | {(5 / 9) * (n - 32):,.3f}")