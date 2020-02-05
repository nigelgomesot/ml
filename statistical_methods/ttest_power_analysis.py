# t-test power analysis

from statsmodels.stats.power import TTestIndPower

effect = 0.80
alpha = 0.05
power = 0.80

analysis = TTestIndPower()
result = analysis.solve_power(effect, power=power, nobs1=None, ratio=1.0, alpha=alpha)
print("sample size: %.3f" % result)
