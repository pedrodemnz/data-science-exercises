v1 = float(input("Qual é o valor 1?"))
v2 = float(input("Qual é o valor 2?"))
v3 = float(input("Qual é o valor 3?"))

if v1 > v2 and v3:
    print(v1,"é o maior valor.")
elif v2 > v1 and v3:
    print(v2,"é o maior valor.")
elif v3 > v1 and v2:
    print(v3,"é o maior valor.")
else:
    print("Os valores são iguais.")