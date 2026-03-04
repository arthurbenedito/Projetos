print("""         -=-=-=-=-=-=-=-=-=-=-=-=
         ANALISADOR DE TRIÂNGULOS
         =--=-=-=-=-=-=-=-=-=-=-=""")
l1=float(input('Insira o valor do primeiro segmento: '))
l2=float(input('insira o valor do segundo segmento: '))
l3=float(input('Insira o valor do terceiro segmento: '))
#if l1<+l2+l3 and l2<l1+l3 and l3<l1+l2
#    print('O triângulo, que tem os lados {}, {}, {}, é factível'.format(l1, l2, l3))
me=l1
if l2<l1 and l2<l3:
    me=l2
if l3<l1 and l3<l1:
    me=l3
ma=l1
if l2>l1 and l2>l3:
    ma=l2
if l3>l1 and l3>l2:
    ma=l3
med=l1
if med<l2<ma:
    med=l2
if med<l3<ma:
    med=l3
if me+med>ma and ma+me>med and med+ma>me:
    print('O triângulo, que tem os lados {}, {}, {}, é factível'.format(l1, l2, l3))
else:
    print('O triângulo, que tem os lados {}, {}, {}, não é factível'.format(l1, l2, l3))
