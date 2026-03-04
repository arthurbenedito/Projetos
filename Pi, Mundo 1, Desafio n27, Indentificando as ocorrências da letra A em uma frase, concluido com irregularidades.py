#from unidecode import unidecode
N=str(input('Digite uma frase: '))
m0=N.lower()
m1=m0.strip()
#m2=unidecode(m1)
#serve para retirar os acentos das frases
I0=m1.count('a')
I1=m1.find('a') + 1
I2=m1.rfind('a') + 1 - m1.count(' ')
print('A frase apresenta a letra A {} vezes\nA primeira letra A é a letra nº{} da frase\nA última letra A é a letra nº {} da frase'.format(I0, I1, I2))
#NÃO ACHEI UM JEITO DE FZR O CÓDIGO FUNCIONAR COM FRASES Q NÃO TÊM A PRIMEIRA PALAVRA COM "A"
