M=0
m=0
for c in range (1, 6):
    p=float(input('O peso da pessoa número {} é de: '.format(c)))
    if c==1:
        p=M
        p=m
    else:
        if p>M:
            M=p
        if p<m:
            m=p
print('O maior peso foi o de {}'.format(M))
print('O menor peso foi o de {}'.format(m))
