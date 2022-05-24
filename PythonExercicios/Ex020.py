import random

alunos = ['João', 'Gabriel', 'Julia', 'Maria']
apresentacao = []
i = 0

while i < len(alunos):
    n = random.randint(0, 3)
    if apresentacao.count(n) == 0:
        apresentacao.append(n)
        i += 1
    
i = 0
print('A ordem de apresentação é:')
while i < len(alunos):
    print('{} - {}'.format(i + 1, alunos[apresentacao[i]]))
    i += 1
