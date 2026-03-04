f=str(input('Digite uma frase: ')).strip().upper()
plvs=f.split()
j=''.join(plvs)
inv=''
inv=j[::-1]
'''for l in range(len(j)-1, -1, -1):
    inv+=j[l]'''
#a variável de controle sempre será do tipo primitivo "int"
if inv==j:
    print('A frase é um palídromo')
    print('O inverso dela {} é {}'.format(j, inv))
else:
    print('Essa frase não é um palídromo')
