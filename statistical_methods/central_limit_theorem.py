# central theorem limit via Dice

from numpy.random import seed
from numpy.random import randint
from numpy import mean
from matplotlib import pyplot

seed(1)

# sample = random value between 1 & 6, 50 times
# mean: of the sample
# experiment: 1000 such samples
# means: collection of mean of all these samples
means = [mean(randint(1, 7, 50)) for _ in range(1000)]

pyplot.hist(means)
pyplot.show()
