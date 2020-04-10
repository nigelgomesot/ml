# visual normality test via qq plot

from numpy.random import seed
from numpy.random import randn
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot

seed(1)

data = 5 * randn(100) + 50

qqplot(data, line='s')
pyplot.show()
