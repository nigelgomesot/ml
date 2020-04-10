# chi-squared distribution PDF

from numpy import arange
from matplotlib import pyplot
from scipy.stats import chi2

sample_space = arange(0, 50, 0.01)
dof = 20

pdf = chi2.pdf(sample_space, dof)

pyplot.plot(sample_space, pdf)
pyplot.show()
