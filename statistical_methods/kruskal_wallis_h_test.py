# kruskal wallis h test

from numpy.random import seed
from numpy.random import rand
from numpy.random import shuffle
from scipy.stats import kruskal

seed(1)

alpha = 0.05

data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
data3 = 52 + (rand(100) * 10)

stat, p = kruskal(data1, data2, data3)
print('Statistic:%.3f, p-value:%.3f' % (stat, p))

if p > alpha:
	print('Same distributions (Fail to Reject H0) | H0')
else:
	print('Different distributions (Reject H0) | H1')

data4 = data1
shuffle(data4)

data5 = data1
shuffle(data5)

stat, p = kruskal(data1, data4, data5)
print('Statistic:%.3f, p-value:%.3f' % (stat, p))

if p > alpha:
	print('Same distributions (Fail to Reject H0) | H0')
else:
	print('Different distributions (Reject H0) | H1')
