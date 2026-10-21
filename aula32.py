try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
except ValueError:
    print('Isso não é um número inteiro')

