# Standard Guassian PDF

from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm

sample_space = arange(-5, 5, 0.001)
mean = 0.0
stdev = 1.0

pdf = norm.pdf(sample_space, mean, stdev)

pyplot.plot(sample_space, pdf)
pyplot.show()
