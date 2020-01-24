# t-test sample means

from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_ind

seed(1)

data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51

stat, p = ttest_ind(data1, data2)
print('statistic=%.3f, p=%.3f' % (stat, p))

alpha = 0.05

if p > alpha:
	print('No difference between sample means (fail to reject H0)')
else:
	print('Some difference between sample means (reject H0)')
