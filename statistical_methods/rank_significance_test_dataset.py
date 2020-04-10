# rank significance test dataset

from numpy.random import seed
from numpy.random import rand

seed(1)

data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)

print('data1: min=%.3f, max=%.3f' % (min(data1), max(data1)))
print('data2: min=%.3f, max=%.3f' % (min(data2), max(data2)))
