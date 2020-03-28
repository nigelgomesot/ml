# rank correlation dataset

from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot

seed(1)

data1 = rand(1000) * 20
data2 = data1 + (rand(1000) * 10)

pyplot.scatter(data1, data2)
pyplot.show()
