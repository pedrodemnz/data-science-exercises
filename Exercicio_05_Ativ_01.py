genero = input('Você é homem ou mulher?')
if genero == 'homem':
    h_homem = float(input('Digite sua altura em metros:'))
    p_homem = (72.7 * h_homem) - 58
    print('Seu peso ideal é de:',p_homem,'Kg')
elif genero == 'mulher':
    h_mulher = float(input('Digite sua altura em metros:'))
    p_mulher = (62.1 * h_mulher) - 44.7
    print('Seu peso ideal é de:',p_mulher,'Kg')


