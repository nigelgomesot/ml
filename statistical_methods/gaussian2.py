from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

# INFO: randn(10000) gives random numbers with mean = 0 & multiplies value with sd = 1
# INFO: (5 * randn(10000) + 50) gives random numbers with mean = 50 & multiplies value with sd = 5
data = 5 * randn(10000) + 50

pyplot.hist(data, bins=100)

pyplot.show()
