# transform data via data resolution

from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

data = randn(100)

data_rounded = data.round(0)

pyplot.hist(data_rounded)
pyplot.show()

pyplot.hist(data)
pyplot.show()
