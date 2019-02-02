#!/usr/bin/env python

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

plt.style.use('ggplot')
#Plotting to our canvas
  
fig = plt.figure()

x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()                    ## 提供图例
plt.grid(True,color='k')        ## 'k' means black
# plt.show()
fig.savefig('/home/tmp/line003.png')  
