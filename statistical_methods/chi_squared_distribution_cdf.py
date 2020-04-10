# chi-squared distribution CDF

from numpy import arange
from matplotlib import pyplot
from scipy.stats import chi2

sample_space = arange(0, 50, 0.01)
dof = 20

cdf = chi2.cdf(sample_space, dof)

pyplot.plot(sample_space, cdf)
pyplot.show()
