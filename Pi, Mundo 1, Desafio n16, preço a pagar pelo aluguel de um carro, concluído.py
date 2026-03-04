D=float(input('Por quantos dias você andou com o carro: '))
Km=float(input('Quantos quilômetros você andou: '))
V=(D*60)+(Km*0.15)
print('O valor a ser pago será igual a {:.2f}'.format(V))
