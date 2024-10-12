import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100)
    total_tentativas = 5
    tentativas = 0
    
    print(f"(DEBUG) O número secreto é: {numero_secreto}")
    print('Bem-vindo ao jogo de adivinhação numérica')
    print('Tente adivinhar o número entre 1 a 100')
    
    while tentativas < total_tentativas:
        try:
            palpite = int(input('Digite seu palpite: '))
        except ValueError:
            print("Por favor, digite um número inteiro.")
            continue
        
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f'Parabéns! Você acertou em {tentativas} tentativa(s)!')
            break
        elif palpite < numero_secreto:
            print('Tente um número maior')  
        else:
            print('Tente um número menor')  
        if tentativas == total_tentativas:
            print(f'Acabaram suas tentativas, o número secreto era {numero_secreto}.')

jogo_de_adivinhacao()
