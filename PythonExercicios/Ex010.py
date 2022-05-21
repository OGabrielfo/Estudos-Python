n = float(input('Informe quantos R$ você tem: '))
d = float(3.27)
print('//APENAS PARA ESTUDO FOI CONSIDERADO R$3,27 COMO VALOR DO DÓLAR//')
print('Você pode comprar ${:.2f} e sobraria R${:.2f}'.format(n//d, n%d))
