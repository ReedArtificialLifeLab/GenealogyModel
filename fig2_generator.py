import genealogy
import dot_creator
import genealogy_inspector as gi
import numpy as np
import sys
import time
import file_manager
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

tests = 10
generations = 20
generations_sizes = 100
a = 0
p = 0
t = 1

parents = 1
ratio_range = [1,2,3,4]

gi.set_parameters({
    'a': a,
    'p': p,
    't': t,
    'generations': generations,
    'generations_sizes': generations_sizes,
    'balanced': False,
    'initial_counts': [1,generations_sizes]
})

# calculate data
for ratio in ratio_range:
    gi.calc_smoothed_percents(parents,ratio,tests)

# plot
gi.initfig()
for ratio in ratio_range:
    gi.plot_percents(parents,ratio)

# save
gi.legend()
gi.savefig("outputs/tmp/test.png")