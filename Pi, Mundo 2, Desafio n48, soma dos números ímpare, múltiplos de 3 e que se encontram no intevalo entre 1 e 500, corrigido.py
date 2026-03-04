n=0
qtd=0
for c in range(1, 501, 2):
    if c%3==0:
        n+=c
        qtd+=+1
print('A soma de todos os números ímpares e múltiplos de 3 no intervalo [0, 500], que engloba {} é igual a {}'.format(qtd,n))
