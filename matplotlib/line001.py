#!/usr/bin/env python

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('classic')
#Plotting to our canvas
  
fig = plt.figure()
plt.plot([1,2,3],[4,5,1])
fig.savefig('/home/tmp/line001.png')  
#Showing what we plotted
# plt.show()
