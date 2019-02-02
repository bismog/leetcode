"""
Visualization of random colors.

Simple plot example with the 20 random colors and its visual representation.
"""
# Based on http://matplotlib.org/examples/color/named_colors.html and https://gist.github.com/adewes/5884820

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import random
import sys
from matplotlib import colors

#====================================================================#

# function to create a random colour, copied from https://gist.github.com/adewes/5884820

def get_random_color(pastel_factor = 0.5):
    return [(x+pastel_factor)/(1.0+pastel_factor) for x in [random.uniform(0,1.0) for i in [1,2,3]]]

#====================================================================#

# function to create a random colour, copied from https://gist.github.com/adewes/5884820

def color_distance(c1,c2):
    return sum([abs(x[0]-x[1]) for x in zip(c1,c2)])

#====================================================================#

# function to create a random colour, copied from https://gist.github.com/adewes/5884820

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

#====================================================================#

# choose 20 random colours:
hex_ = []
mycolours = []
names = []
for i in range(1,21):
    mycolour = generate_new_color(mycolours,pastel_factor = 0.9)
    mycolours.append(mycolour)
    myhex = colors.rgb2hex(mycolour)
    hex_.append(myhex)
    names.append(myhex)

n = len(hex_)
ncols = 4
nrows = int(np.ceil(1. * n / ncols))
fig, ax = plt.subplots()

X, Y = fig.get_dpi() * fig.get_size_inches()

# row height
h = Y / (nrows + 1)
# col width
w = X / ncols

for (i, color) in enumerate(hex_):
    name = names[i]
    col = i % ncols
    row = int(i / ncols)
    y = Y - (row * h) - h

    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)

    ax.text(xi_text, y, name, fontsize=(h * 0.075),
            horizontalalignment='left',
            verticalalignment='center')

    # Add extra black line a little bit thicker to make
    # clear colors more visible.
    ax.hlines(y, xi_line, xf_line, color='black', linewidth=(h * 0.7))
    ax.hlines(y + h * 0.1, xi_line, xf_line, color=color, linewidth=(h * 0.6))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0,
                    hspace=0, wspace=0)
plt.savefig("/home/tmp/random_colour_key.png")
