# transform data via removing longtails

from numpy.random import seed
from numpy.random import randn
from numpy.random import rand
from numpy import append
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 10
tail = 10 + (rand(10) * 100)

data_with_tail = append(data, tail)

pyplot.hist(data_with_tail)
pyplot.show()

data_without_tail = [x for x in data if x < 25]

pyplot.hist(data_without_tail)
pyplot.show()
