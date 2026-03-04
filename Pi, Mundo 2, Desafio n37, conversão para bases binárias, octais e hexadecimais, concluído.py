N=int(input('Informe o número desejado: '))
print('Digite 1 para binário \nDigite 2 para octal \nDigite 3 para hexadecimal ')
E=int(input('Escolha base numérica: '))
if E==1:
    bi=(bin(N)[2:])
    print('O número {} correponde a {} em binário'.format(N, bi))
elif E==2:
    oc=(oct(N)[2:])
    print('O número {} corresponde a {} em octal'.format(N, oc))
elif E==3:
    he=(hex(N)[2:])
    print('O número {} corresponde a {} em hexadecimal'.format(N, he))
else:
    print('Falha no sistema, tente novamente')
print('='*15)
print('FIM DO PROGRAMA')
print('='*15)
