import math
c1=float(input('Digite o valor do cateto oposto: '))
c2=float(input('Digite o valor do cateto adjacente:'))
H=(math.hypot(c1, c2))
print('O valor da hipotenusa desse triângulo equivale a {:.2f}'.format(H))
