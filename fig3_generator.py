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

tests = 100
generations = 2
generations_sizes = 1000
a = 0
p = 0
t = 1

parents_range = [1,2,3]
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
gi.calc_smoothed_percents_range(parents_range,ratio_range,tests)
gi.calc_first_slopes(parents_range,ratio_range)

# plot
gi.initfig()
for ratio in ratio_range:
    gi.plot_first_slopes_parents(parents_range,ratio,regression_type="linear")

# save
gi.legend()
gi.savefig("outputs/tmp/test.png")