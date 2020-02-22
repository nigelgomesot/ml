# parametric tolerance interval

from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import sqrt
from scipy.stats import norm
from scipy.stats import chi2

seed(1)

data = 5 * randn(100) + 50

# specify dof
n = len(data)
dof = n - 1

# specify coverage
prop = 0.95
prop_inv = (1.0 - prop) / 2.0
gauss_critical = norm.ppf(prop_inv)
print('Gaussian critical value: %.3f (coverage=%d%%)' % (gauss_critical, prop*100))

# specify confidence
prob = 0.99
prob_inv = (1.0 - prob)
chi_critical = chi2.ppf(prob_inv, dof)
print('Chi-squared critical value: %.3f (confidence=%d%%, dof=%d)' % (chi_critical, prob*100, dof))

# calculate tolerance
interval = sqrt((dof * (1 + 1/n) * gauss_critical**2) / chi_critical)
print('Tolenace interval: %.3f' % interval)

# summarize
data_mean = mean(data)
lower, upper = data_mean - interval, data_mean + interval
print('%.2f to %.2f covers %d%% of data with a confidence of %d%%' % (lower, upper, prop*100, prob*100))
