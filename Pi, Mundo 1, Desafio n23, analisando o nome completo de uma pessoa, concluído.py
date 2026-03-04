N=input('Escreva o seu nome completo: ')
print('Analisando...')
Ma=N.upper()
Mi=N.lower()
L=len(N)-N.count(' ')
P=N.split()
Pn=P[0]
nPn=len(Pn)
print('O seu nome completo com letras maiúsculas é: {}\nO seu nome completo com letras minúsculas é {}\nO seu nome tem um total de {} letras\nO seu primeiro nome é {} e ele tem {} letras'.format(Ma, Mi, L, Pn, nPn))
