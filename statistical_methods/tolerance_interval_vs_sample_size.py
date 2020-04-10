# tolerance interval vs sample size

from numpy.random import seed
from numpy.random import randn
from numpy import sqrt
from scipy.stats import chi2
from scipy.stats import norm
from matplotlib import pyplot

seed(1)

sizes = range(5, 15)

for n in sizes:
	data = 5 * randn(n) + 50

	dof = n - 1

	prop = 0.95
	prop_inv = (1 - prop) / 2
	gauss_critical = norm.ppf(prop_inv)

	prob = 0.99
	prob_inv = (1.0 - prob)
	chi_critical = chi2.ppf(prob_inv, dof)

	tol = sqrt((dof * (1 + (1/n)) * gauss_critical**2) / chi_critical)

	pyplot.errorbar(n, 50, yerr=tol, color='blue', fmt='o')

pyplot.show()
