#!/usr/bin/env python

from os import listdir
import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
from matplotlib import colors
import random

def get_random_color(pastel_factor = 0.5):
    return [(x+pastel_factor)/(1.0+pastel_factor) for x in [random.uniform(0,1.0) for i in [1,2,3]]]

def color_distance(c1,c2):
    return sum([abs(x[0]-x[1]) for x in zip(c1,c2)])

def generate_new_color(existing_colors,pastel_factor = 0.5):
    max_distance = None
    best_color = None
    for i in range(0,100):
        color = get_random_color(pastel_factor = pastel_factor)
        if not existing_colors:
            return color
        best_distance = min([color_distance(color,c) for c in existing_colors])
        if not max_distance or best_distance > max_distance:
            max_distance = best_distance
            best_color = color
    return best_color

# choose 20 random colours:
hex_ = []
mycolours = []
names = []
for i in range(20):
    mycolour = generate_new_color(mycolours,pastel_factor = 0.9)
    mycolours.append(mycolour)
    myhex = colors.rgb2hex(mycolour)
    hex_.append(myhex)
    names.append(myhex)


plt.style.use('classic')
# More style at: https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
# plt.style.use('seaborn-pastel')
fig = plt.figure()

x = [15.0,30.0,45.0,60.0]           ## 1 for 1 hypervisor(15instances), 2 for 2 hypervisors(30instances), and so on.

# Get data from files in directory /home/tmp/perf/all_in_one
all_data = []
data_path = "/home/tmp/perf/all_in_one/"
# data_path = "/run/data/"
file_names = listdir(data_path)
for file_name in file_names:
    fn = '{}{}'.format(data_path,file_name)
    with open(fn) as f:
        data = f.readlines()
        all_data.append(data)

# y = [75,104,274,312]
# y2 = [95,124,266,302]

# plt.scatter(x,y, label='high income low saving',color='r')
# plt.scatter(x1,y1,label='low income high savings',color='b')
# plt.scatter(x,y)
# plt.scatter(x,y2)
for data in all_data:
    try:
        float_data = [float(d) for d in data]
        plt.scatter(x, float_data, color=random.choice(hex_))
    except ValueError,e:
        continue
        # print "error",e,"with value: \'",d,"\'"
plt.xlabel('x hypervisor 15x instances')
plt.ylabel('create time(sec)')
plt.title('Concurrent Creating Instances')
# plt.grid(True, linestyle='-', color='gray')        ## 'k' means black
plt.grid(True)        ## 'k' means black
# plt.legend()

fig.savefig('/home/tmp/scatter002.png')
