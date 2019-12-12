# generate random numbers

from random import seed
from random import random
from random import randint

print('\nseed ensures random function is deterministic')
seed(1)
print(random(), random(), random())

seed(1)
print(random(), random(), random())

print('\nfloating point values')
seed(1)
for _ in range(10):
	value = random()
	print(value)

print('\n integer values')
seed(1)
for _ in range(10):
	value = randint(0, 10)
	print(value)
