# bootstrap resampling

from sklearn.utils import resample

data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

boot = resample(data, replace=True, n_samples=4, random_state=1)
print('Bootstrap sample: %s' % boot)

oob = [x for x in data if x not in boot]
print('OOB sample: %s' % oob)
