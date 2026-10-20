"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

username = input('Digite o seu username:')
idade = input('Digite a sua idade:')


if username and idade:
    print(f'O seu username é {username}')
    print(f'A sua idade é {idade}')
    print(f'Seu nome invertido é {username[::-1]}')
    print(f'Seu username contém {len(username)} caractéres')
    print(f'A primeira letra do seu username é {username[0]}')
    print(f'A ultima letra do seu username é {username[-1]}')
    if " " in username:
        print('Seu username contém espaços')
    else:
        print('Seu username não contém espaços')
else:
    print('Você não preencheu os campos necessários')
