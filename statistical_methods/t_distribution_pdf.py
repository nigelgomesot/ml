# t-distribution PDF

from numpy import arange
from matplotlib import pyplot
from scipy.stats import t

sample_space = arange(-5, 5, 0.001)
dof = len(sample_space) - 1

pdf = t.pdf(sample_space, dof)

pyplot.plot(sample_space, pdf)
pyplot.show()
