# shapiro wilk normality test

from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro

seed(1)

data = 5 * randn(100) + 50

stat, p_value = shapiro(data)

print("statistic=%.3f, p_value=%.3f" % (stat, p_value))

alpha = 0.05

if p_value <= alpha:
	print('sample does not seem like Gaussian, Reject H0 (H1)')
else:
	print('sample seems like Gaussian, Fail to Reject H0 (H0)')
