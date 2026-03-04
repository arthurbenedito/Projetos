l1=float(input('Informe o valor do primeiro lado: '))
l2=float(input('Informe o valor do segundo lado: '))
l3=float(input('Informe o valor do terceiro lado: '))
if l1<l2+l3 and l2<l3+l1 and l3<l1+l2:
    print('O triângulo é factível ')
if l1>l2+l3 or l2>l1+l3 or l3>l1+l2:
    print('O triângulo não é factível')
elif l1!=l2!=l3:
    print('Esse triângulo é escaleno')
elif l1==l2!=l3 or l1!=l2==l3:
    print('Esse triângulo é isósceles')
elif l1==l2==l3:
    print('Esse triângulo é equilátero')
