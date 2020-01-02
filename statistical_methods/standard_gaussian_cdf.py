# Standard gaussian CDF

from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm

sample_space = arange(-5, 5, 0.001)

cdf = norm.cdf(sample_space)

pyplot.plot(sample_space, cdf)
pyplot.show()
