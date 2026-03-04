dn=int(input('Insira a sua data de nascimento: '))
I=2026-dn
print('O atleta tem {} anos'.format(I))
if I<=9:
    print('O atleta é classificado como mirim')
elif 10<I<=14:
    print('O atleta é classificado como infantil')
elif 15<I<=19:
    print('O atleta é classificado como junior')
elif 20<I<=25:
    print('O atleta é classificado como sênior')
else:
    print('O atleta é classificado como master')
