import random
nc=random.randint(0,5)
nu=int(input('Escoha um número entre 0 e 5 : '))
if nc==nu:
    print('Número certo ! Prabéns, você venceu !')
else:
    print('Número errado ! O que eu pensei foi {} !'.format(nc))
