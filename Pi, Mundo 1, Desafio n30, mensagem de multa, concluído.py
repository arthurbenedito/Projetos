v=float(input('A qual velocidade você estava trafegando na via ? '))
va=(v-80)
mu=va*7
if v>80:
    print('Você receberá uma multa de {} reais em menos de 20 dias úteis, vide que a velocidade era {} km/h superior à permitida na via'.format(mu, va))
