#!/usr/bin/env python

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')
fig = plt.figure()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.subplot(223)
plt.plot(t1, f(t1), 'bo', t2, f(t2))
plt.subplot(224)
plt.plot(t2, np.cos(2*np.pi*t2))

fig.savefig('/home/tmp/multiplot.png')
