print('-='*11)
print('PROGRESSÃO ARITMËTICA')
print('-='*11)
t0=int(input('Informe o valor do primeiro termo: '))
r=int(input('Informe o valor da razão da P.A: '))
t10=t0+(11-1)*r
for c in range(t0, t10, r):
    print(c, end=' --> ')
print('FIM')
