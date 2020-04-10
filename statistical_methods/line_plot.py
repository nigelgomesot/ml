# draw line plot

from numpy import sin
from matplotlib import pyplot

x = [x*0.1 for x in range(100)]

y = sin(x)

pyplot.plot(x, y)

pyplot.show()
