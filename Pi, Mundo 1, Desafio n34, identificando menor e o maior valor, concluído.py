n1=float(input('Digite o primeiro valor: '))
n2=float(input('Digite o segundo valor: '))
n3=float(input('Digite o terciero valot: '))
#Verificando qual número é menor
me=n1
if n2<n1 and n2<n3:
    me=n2
if n3<n1 and n3<n2:
    me=n3
print('O menor valor é {}'.format(me))
#Verificando qual número é maior
ma=n1
if n2>n1 and n2>n3:
    ma=n2
if n3>n1 and n3>n2:
    ma=n3
print('O maior valor é {}'.format(ma))
