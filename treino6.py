nome = input('Qual o seu nome?: ')
tamanho = (len(nome))

if tamanho <= 4:
    print('O seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')