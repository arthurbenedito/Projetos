from random import choice, shuffle
n1=str(input('Digite o nome do primeiro aluno: '))
n2=str(input('Digite o nome do segundo aluno: '))
n3=str(input('Digite o nome do terceiro aluno: '))
n4=str(input('Digite o nome do quarto aluno: '))
L=[n1, n2, n3, n4 ]
#R=random.shuffle(L)
#print('O aluno escolhido foi {}'.format(L[0]))
R=random.choice(L)
print('O aluno escolhido foi {}'.format(R))
