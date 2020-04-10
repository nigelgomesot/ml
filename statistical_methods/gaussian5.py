# calculate variance measures

from numpy.random import seed
from numpy.random import randn
from numpy import var
from numpy import std

seed(1)

data = 5 * randn(10000) + 50

var_result = var(data)
print("Variance: %.3f" % var_result)

std_result = std(data)
print("Standard Deviation: %.3f" % std_result)

