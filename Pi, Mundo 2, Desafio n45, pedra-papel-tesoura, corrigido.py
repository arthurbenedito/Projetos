from random import randint
from time import sleep
I=('Pedra', 'Papel', 'Tesoura')
C=randint(0,2)
print("""Suas escolhas:
[0] Pedra
[1] Papel
[2] Tesoura""")
J=int(input('Qual a sua jogada ? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO !!!!')
sleep(0.5)
print('-='*14)
print('O computador escolheu {}'.format(I[C]))
print('O jogador escolheu {}'.format(I[J]))
print('-='*14)
if C==0:
    if J==0:
        print('Empate')
    elif J==1:
        print('Jogador venceu !')
    elif J==2:
        print('Computador venceu !')
    else:
        print('Jogada inválida')
elif C==1:
    if J==0:
        print('Computador venceu !')
    elif J==1:
        print('Empate')
    elif J==2:
        print('Jogador venceu !')
    else:
        print('Jogada inválida')
elif C==2:
    if J==0:
        PRINT('Jogador venceu !')
    elif J==1:
        print('Computador venceu ! ')
    elif J==2:
        print('Empate')
    else:
        print('Jogada inválida')
