# linear regression prediction interval

from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot

seed(1)

x = 20 * randn(1000) + 100
y = x + (10 * randn(1000) + 50)

print("x: mean=%.3f, std:%.3f" % (mean(x), std(x)))
print("y: mean=%.3f, std:%.3f" % (mean(y), std(y)))

pyplot.scatter(x, y)
pyplot.show()
