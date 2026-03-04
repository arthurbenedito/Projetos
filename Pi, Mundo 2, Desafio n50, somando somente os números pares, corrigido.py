a1=0
a2=0
for c in range(1,7):
    n=int(input('Digite o {} valor: '.format(c)))
    if n%2==0:
        a1+=n
        a2+=1
print('Dentre os números que você informou, {} são pares, e {} é o somatório deles'.format(a2, a1))
