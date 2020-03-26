# five number summary

from numpy import percentile
from numpy.random import seed
from numpy.random import rand

seed(1)

data = rand(1000)

data_quartiles = percentile(data, [25, 50, 75])

data_min, data_max = data.min(), data.max()

print('Min: %.3f' % data_min)
print('Q1: %.3f' % data_quartiles[0])
print('Median: %.3f' % data_quartiles[1])
print('Q3: %.3f' % data_quartiles[2])
print('Max: %.3f' % data_max)
