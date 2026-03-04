D=float(input('Informe a distância a ser viajada: '))
if D<=200:
    Vd = D * 0.50
else:
    Vd = D * 0.45
print('O valor da passagem será de R${:.2f}'.format(Vd))
