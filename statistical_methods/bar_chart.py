# draw bar chart

from random import seed
from random import randint
from matplotlib import pyplot

seed(1)

x = ['red', 'green', 'blue']
y = [randint(0, 100), randint(0, 100), randint(0, 100)]

pyplot.bar(x, y)

pyplot.show()
