from math import hypot

catOp = float(input('Informe o valor do cateto oposto: '))
catAd = float(input('Informe o valor do cateto adjacente: '))
hip = hypot(catAd, catOp)

print('O valor da hipostenusa é {:.2f}'.format(hip))
