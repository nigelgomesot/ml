# draw scatter plot

from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

x = 20 * randn(1000) + 100
y = x + (10 * randn(1000) + 50)

pyplot.scatter(x, y)

pyplot.show()
