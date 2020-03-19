# transform data via sample size

from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

data1 = 50 * randn(10) + 100

pyplot.hist(data1)
pyplot.show()


data2 = 50 * randn(100) + 100

pyplot.hist(data2)
pyplot.show()
