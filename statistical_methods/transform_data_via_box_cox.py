# transform data via box cox

from numpy.random import seed
from numpy.random import randn
from numpy import exp
from scipy.stats import boxcox
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 100

data_exp = exp(data)
pyplot.hist(data_exp)
pyplot.show()

data_boxcox = boxcox(data_exp, 0)
pyplot.hist(data_boxcox)
pyplot.show()
