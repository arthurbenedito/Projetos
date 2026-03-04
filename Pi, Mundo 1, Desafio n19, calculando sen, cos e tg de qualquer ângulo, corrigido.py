import math
a=int(input('Digite o valor do ângulo qeu você deseja: '))
a1=math.radians(a)
s=math.sin(a1)
c=math.cos(a1)
t=math.tan(a1)
print('O valor de seno de {} é igual a {:.2f}\nO valor de cosseno de {} é igual a {:.2f}\nO valor da tangente de {} é igual a {:.2f}'.format(a, s, a, c, a, t))
