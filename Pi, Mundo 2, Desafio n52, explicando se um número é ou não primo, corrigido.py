n=int(input('Informe um número : '))
tot=0
for c in range (1, n+1):
    if n%c==0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if tot==2:
    print('\n\033[mEsse número é divisível por 2 números, então ele é primo')
else:
    print('\n\033[mEsse número é divisível por {} outros números, então ele não é primo'.format(n - tot))
