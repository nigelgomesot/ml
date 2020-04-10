# visual normality test via histogram plot

from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 50

print('mean=%.3f, stdev:%.3f' % (mean(data), std(data)))

pyplot.hist(data)
pyplot.show()
