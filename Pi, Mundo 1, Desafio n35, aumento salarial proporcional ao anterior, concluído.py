Sb=float(input('Digite o seu salário: '))
if Sb<=1250:
    Sa=Sb*1.15
else:
    Sa=Sb*1.10
print('O seu salário, depois desse aumento, será igual a R${:.2f}. Antes ele era igual a R${}.'.format(Sa,Sb))
