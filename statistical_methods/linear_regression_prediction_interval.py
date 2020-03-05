# linear regression prediction interval

from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from numpy import sum as arraysum
from numpy import sqrt
from scipy.stats import linregress

seed(1)

x = 20 * randn(1000) + 100
y = x + (10 * randn(1000) + 50)
print("x: mean=%.3f, std:%.3f" % (mean(x), std(x)))
print("y: mean=%.3f, std:%.3f" % (mean(y), std(y)))

b1, b0, r_value, p_value, std_err = linregress(x, y)
print("b0:%.3f, b1:%.3f" % (b0, b1))

yhat = b0 + b1 * x

# estimate stdev of hat
sum_errors = arraysum((y - yhat)**2)
stdev = sqrt(1/(len(y) - 2) * sum_errors)

pyplot.scatter(x, y)
pyplot.plot(x, yhat, color='r')
pyplot.show()
