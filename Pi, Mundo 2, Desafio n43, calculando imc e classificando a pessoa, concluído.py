alt=float(input('Informe a sua altura, em metros: '))
peso=float(input('Informe o seu peso: '))
imc=peso/(alt**2)
print('O imc dessa pessoa é de {}'.format(imc))
if imc<18.5:
    print('Você está abaixo do peso ideal')
elif 18.5<imc<25:
    print('Você está no peso ideal, parabéns !!')
elif 25<imc<30:
    print('Você está com sobrepeso, melhore a sua dieta !')
elif 30<imc<40:
    print('Você está com obeidade, se cuide melhor !')
else :
    print('Você está com obesidade mórbida! Tome cuidado! Você só tem uma vida')
#os valores para a validação do imc talvez estejam incorretos de acordo com ciência
