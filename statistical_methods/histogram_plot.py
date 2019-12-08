# draw histogram

from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

x = randn(1000)

pyplot.hist(x)

pyplot.show()
