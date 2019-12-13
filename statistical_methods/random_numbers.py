# generate random numbers

from random import seed
from random import random
from random import randint
from random import gauss
from random import choice
from random import sample
from random import shuffle

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

print('\ninteger values')
seed(1)
for _ in range(10):
	value = randint(0, 10)
	print(value)

print('\ngaussian values')
seed(1)
for _ in range(10):
	# gauss(mean, sd)
	value = gauss(0, 1);
	print(value)

print('\nsequence')
sequence = [i for i in range(20)]
print(sequence)

print('\nchoice from a list')
seed(1)
for _ in range(5):
	value = choice(sequence)
	print(value)

print('\nsample from a list')
seed(1)
value = sample(sequence, 5)
print(value)

print('\nshuffle list')
seed(1)
print('sequence')
print(sequence)
value = shuffle(sequence)
print('shuffle')
print(sequence)
