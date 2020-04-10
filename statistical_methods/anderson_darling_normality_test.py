# anderson darling normality test

from numpy.random import seed
from numpy.random import randn
from scipy.stats import anderson

seed(1)

data = 5 * randn(100) + 50

result = anderson(data)

print('Statistic:%.3f' % result.statistic)

p = 0
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]

	if result.statistic <  cv:
		print("sl:%.3f, cv:%.3f; sample seems like Gaussian, Fail to Reject H0 (H0)" % (sl, cv))
	else:
		print("sl:%.3f, cv:%.3f; sample does not seem like Gaussian, Reject H0 (H1)" % (sl, cv))
