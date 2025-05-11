valores = []
contador = 0

while True:
    entrada = input('Digite um valor ou digite "fim" para sair: ')
    if entrada.lower() == "fim":
        break
    try:
        valor = float(entrada)
        valores.append(valor)
        if valor > 20:
            contador += 1
    except ValueError:
        print("Digite um número válido ou 'fim' para sair.")

if valores:
    quant = len(valores)
    soma = sum(valores)
    media = soma / quant

    print("Resultados:")
    print(f"Quantidade de valores: {quant}")
    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Quantidade de valores maiores que 20: {contador}")
else:
    print("Nenhum valor foi digitado.")
