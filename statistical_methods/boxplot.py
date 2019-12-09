# draw boxplot

from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

seed(1)

x = [randn(1000), 5 * randn(1000), 10 * randn(1000)]

pyplot.boxplot(x)

pyplot.show()
