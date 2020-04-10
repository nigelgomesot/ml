# classification accuracy via confidence interval

from statsmodels.stats.proportion import proportion_confint

correct_predictions = 88
total_predictions = 100
critical_value = 0.05

lower, upper = proportion_confint(correct_predictions, total_predictions, critical_value)
print('lower=%.3f, upper=%.3f' % (lower, upper))
