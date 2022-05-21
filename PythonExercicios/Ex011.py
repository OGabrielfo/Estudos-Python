alt = float(input('Informe em metros a altura da parede a ser pintada: '))
lar = float(input('Informe em metros a largura da parede a ser pintada: '))
a = alt * lar
print('Serão necessários {:.1f} litros de tinta.'.format(a/2))
