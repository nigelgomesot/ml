# mann whitney u test

from numpy.random import seed
from numpy.random import rand
from numpy.random import shuffle
from scipy.stats import mannwhitneyu

seed(1)

alpha = 0.05

data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)

stat, p = mannwhitneyu(data1, data2)
print('Statistic:%.3f, p-value:%.3f' % (stat, p))

if p > alpha:
	print('Same distribution (Fail to Reject H0) | H0')
else:
	print('Different distribution (Reject H0) | H1')

data3 = data1
shuffle(data3)

stat, p = mannwhitneyu(data1, data3)
print('Statistic:%.3f, p-value:%.3f' % (stat, p))

if p > alpha:
	print('Same distribution (Fail to Reject H0) | H0')
else:
	print('Different distribution (Reject H0) | H1')
