# law of large numbers

from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import array
from matplotlib import pyplot

seed(1)

sizes = list()
for x in range(10, 20000, 200):
	sizes.append(x)

means = [mean(5 * randn(size) + 50) for size in sizes]

pyplot.scatter(sizes, array(means) - 50)

pyplot.show()
