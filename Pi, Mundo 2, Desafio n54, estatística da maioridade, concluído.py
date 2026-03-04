from datetime import date
aat=date.today().year
M=0
m=0
for c in range(1, 8):
    dn=int(input('Informe a data de nascimento: '))
    id=aat-dn
    if id>=18:
        M+=1
    else:
        m+=1
print('Segundo os dados informados, {} pessoas são maior(es) de idade, enquanto {} são menor(es) e ainda não desenvolveram completamente o cérebro'.format(M, m))
