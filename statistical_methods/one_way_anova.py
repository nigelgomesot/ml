# one way ANOVA

from numpy.random import seed
from numpy.random import randn
from scipy.stats import f_oneway

seed(1)

data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 50
data3 = 5 * randn(100) + 52

statistic, p = f_oneway(data1, data2, data3)
print("statistic=%.3f, p=%.3f" % (statistic, p))

alpha = 0.05
if p > alpha:
	print("all sample distributions are same (fail to reject H0)")
else:
	print("Some sample distributions are not same (reject H0)")
