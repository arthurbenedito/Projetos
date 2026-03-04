N=int(input('Informe a sua data de nascimento: '))
if N>2008:
    id= 2026 - N
    tr=18-id
    da= tr+2026
    print('Você tem {}.\n Faltam {} ano(s) para o alistamento.\nSeu alistamento será em {}'.format(id, tr, da))
elif N<2008:
    id=2026-N
    tr=id-18
    da=2026-tr
    print('Você tem {} anos\nSeu alistamento deveria ter sido feito {} ano(s) atrás\nVocê deveria ter se alsitado em {}'.format(id, tr, da))
else:
    print('Você tem 18 anos e deve se alistar imediatamente')
