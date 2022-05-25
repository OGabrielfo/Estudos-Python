from random import shuffle

alunos = ['João', 'Gabriel', 'Julia', 'Maria']
shuffle(alunos)

i = 0
print('A ordem de apresentação é:')
while i < len(alunos):
    print('{} - {}'.format(i + 1, alunos[i]))
    i += 1
