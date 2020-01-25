# Paired t-test

from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_rel

seed(1)

data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51

stat, p = ttest_rel(data1, data2)
print("statistic=%.3f, p=%.3f" % (stat, p))

alpha = 0.05
if p > alpha:
	print("paired sample distributions are equal (fail to reject HO)")
else:
	print("paired sample distributions are not equal (reject HO)")
