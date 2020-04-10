# chi squared distribution PPF

from scipy.stats import chi2

p = 0.95
dof = 10

value = chi2.ppf(p, dof)
print(value)

p = chi2.cdf(value, dof)
print(p)
