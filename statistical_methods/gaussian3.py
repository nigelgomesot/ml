# calculate mean from a sample.

from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import median

seed(1)

data = 5 * randn(10000) + 50

mean_result = mean(data)

print('Mean: %3f' % mean_result)

median_result = median(data)

print('Median: %3f' % median_result)
