# t-distribution PPF

from scipy.stats import t

p = 0.95
dof = 10

value = t.ppf(p, dof)
print(value)

p = t.cdf(value, dof)
print(p)
