sa=float(input('Informe o seu salário: '))
vc=float(input('Informe o valor da casa a comprar: '))
tq=float(input('Informe em até quanto tempo, em anos, você irá quitar a dívida da casa: '))
pm=vc/tq
qp=sa/pm
if sa<pm:
    print('O empréstimo não poderá ser concedido, vide que o valor da parcela ultrapassa 30% do valor do seu salário')
elif sa>pm:
    print('Parabéns, o seu empréstimo foi aprovado ! O valor médio das parcelas mensais e a quantidade delas, respectivamente, é de {}'.format(pm, qp))
