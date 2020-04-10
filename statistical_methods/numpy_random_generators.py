# generate numbers via numpy library

from numpy.random import seed
from numpy.random import rand
from numpy.random import randint
from numpy.random import randn
from numpy.random import shuffle

print('\n using seed')
seed(1)
print(rand(3))

seed(1)
print(rand(3))

print('\n floating points')
seed(1)
values = rand(10)
print(values)

print('\n integer values')
seed(1)
values = randint(1000, 2000, 10)
print(values)

print('\n gaussian values')
seed(1)
values = randn(10)
print(values)

print('\n shuffle values')
seed(1)
sequence = [i for i in range(20)]
print(sequence)
shuffle(sequence)
print(sequence)
