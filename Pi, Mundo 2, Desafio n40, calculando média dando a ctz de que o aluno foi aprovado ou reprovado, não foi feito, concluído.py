n1=float(input('Digite a sua nota parcial:  '))
n2=float(input('Digite a sua nota global: '))
m=(n1+n2)/2
print('Tirando {} e {}, a sua média fica igual a {}'.format(n1, n2, m))
if m>=7:
    print('O aluno foi aprovado !')
elif 5<m<6.9:
    print('O aluno ficou de recuperação !')
elif m<5:
    print('O aluno foi reprovado !')
print('='*15)
print('FIM DO PROGRAMA')
print('='*15)
