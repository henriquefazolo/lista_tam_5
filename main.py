'''
Crie um vetor de int vetA com tamanho 5 e mostre na tela os valores de seus elementos;
'''

import random
vetA = []
while len(vetA) < 5:
    vetA.append(random.randint(1, 100))
print(vetA)