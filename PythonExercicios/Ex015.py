dias = float(input('Informe quantos dias o carro ficou alugado: '))
km = float(input('Informe a distância em KM percorrida: '))
diaria, pkm = 60, 0.15
precofinal = (dias * diaria)+(km * pkm)
print('O valor total do aluguel é de R${:.2f}'.format(precofinal))
