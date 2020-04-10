# pearson correlation

from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr

seed(1)

data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

corr, p = pearsonr(data1, data2)

print('Pearsons correlation %.3f' % corr)

alpha = 0.05

if p > alpha:
	print('no correlation [fail to reject H0]')
else:
	print('some correlation [reject H0]')
