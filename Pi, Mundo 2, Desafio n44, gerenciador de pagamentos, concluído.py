p=float(input('Informe o valor das compras: '))
fp=int(input('[1] à vista no dinheir/cheque\n[2] à vista o cartão\n[3] em duas vezes no cartão\n[4] em 3 ou mais vezes no cartão\nEscolha a sua forma de pagamento: '))
par=int(input('Em até quantas parcelas você deseja pagar ?'))
if fp==1:
    p1=p*(0.9)
    print('O valor das compras será igual a R${}, vide q você pagou à vista em dinheiro ou cheque e há 10% de desconto nessa modalidade'.format(p1))
elif fp==2:
    p2=p*(0.95)
    print('O valor das compras será igual a R${}, vide que você pagou à vista no cartão, e nessa modalidade há 5% de descconto'.format(p2))
elif fp==3 and par<=2:
    print('Você pagou em duas vezes no cartão. O valor das compras será de R${}'.format(p))
elif fp==4 and par>=3:
    p4=p*(1.2)
    vpar=p4/par
    print('Você pagou em {} vezes no cartão. O valor das suas compras é de R${} e cada parcela terá o valor de R${} '.format(par, p4, vpar))
else:
    print('Erro no sistema. Comece o processo novamente')
