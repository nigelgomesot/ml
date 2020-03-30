# kendall rank correlation

from numpy.random import rand
from numpy.random import seed
from scipy.stats import kendalltau

seed(1)

data1 = rand(1000) * 20
data2 = (rand(1000) * 10) + data1

coef, p = kendalltau(data1, data2)
print('Kendall correlation coeffecient:%.3f' % coef)
print('p-value:%.3f' % p)

alpha = 0.05
if p > alpha:
	print('Samples are uncorrelated (Fail to Reject H0) H0')
else:
	print('Samples are correlated (Reject H0) H1')

data3 = (rand(1000) * 10)

coef, p = kendalltau(data1, data3)
print('Kendall correlation coeffecient:%.3f' % coef)
print('p-value:%.3f' % p)

alpha = 0.05
if p > alpha:
	print('Samples are uncorrelated (Fail to Reject H0) H0')
else:
	print('Samples are correlated (Reject H0) H1')
