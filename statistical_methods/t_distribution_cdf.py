# t-distribution CDF

from numpy import arange
from matplotlib import pyplot
from scipy.stats import t

sample_space = arange(-5, 5, 0.001)
dof = len(sample_space) - 1

cdf = t.cdf(sample_space, dof)

pyplot.plot(sample_space, cdf)
pyplot.show()
