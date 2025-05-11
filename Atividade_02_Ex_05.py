la = float(input('Qual o lado "a" do triângulo?'))
lb  = float(input('Qual o lado "b" do triângulo?'))
lc = float(input('Qual o lado "c" do triângulo?'))

if (la + lb > lc) and (la + lc > lb) and (lb + lc > la):
    if la == lb == lc:
        print("O triângulo é equilátero.")
    elif la != lb != lc:
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isósceles.")
else:
    print("Não é um triângulo.")










