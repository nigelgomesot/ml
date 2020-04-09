# chi squared test

from scipy.stats import chi2_contingency
from scipy.stats import chi2

table = [
	[10, 20, 30],
	[6,  9,  17]
]

print(table)

stat, p, dof, expected = chi2_contingency(table)

print('dof=%d' % dof)

print(expected)

prob = 0.95
critical = chi2.ppf(prob, dof)

print('probability=%.3f, critical-value=%.3f, statistic=%.3f' % (prob, critical, stat))

if abs(stat) >= critical:
	print('Dependent, (Reject H0) H1')
else:
	print('Independent, (Fail to Reject H0) H0')

alpha = 1 - prob

print('significance=%.3f, p=%.3f' % (alpha, p))

if p <= alpha:
	print('Dependent, (Reject H0) H1')
else:
	print('Independent, (Fail to Reject H0) H0')
