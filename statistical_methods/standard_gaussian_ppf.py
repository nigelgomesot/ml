# Standard Gaurssion PPF

from scipy.stats import norm

p = 0.95

value = norm.ppf(p)
print(value)

p = norm.cdf(value)
print(p)
