# covariance

from numpy.random import randn
from numpy.random import seed
from numpy import cov

seed(1)

data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

covariance = cov(data1, data2)
print(covariance)
