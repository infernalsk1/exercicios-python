import secrets
import string

try:
    tamanho = int(input("Quantos caracteres a senha deve ter? (mínimo 12): "))

    if tamanho < 12:
        print("Use pelo menos 12 caracteres para uma senha forte.")
    else:
        minusculas = string.ascii_lowercase
        maiusculas = string.ascii_uppercase
        numeros = string.digits
        simbolos = "!@#$%&*?"
        todos = minusculas + maiusculas + numeros + simbolos

        # garante pelo menos um de cada tipo
        senha = [
            secrets.choice(minusculas),
            secrets.choice(maiusculas),
            secrets.choice(numeros),
            secrets.choice(simbolos),
        ]

        # completa o restante com caracteres aleatórios
        for _ in range(tamanho - 4):
            senha.append(secrets.choice(todos))

        # embaralha para os 4 primeiros não ficarem sempre na mesma ordem
        secrets.SystemRandom().shuffle(senha)

        print("Sua senha:", "".join(senha))
except ValueError:
    print("Digite um número inteiro.")