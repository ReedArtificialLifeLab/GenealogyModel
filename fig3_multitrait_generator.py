import genealogy_multitraits_inspector as gi
import numpy as np

# parents_range = [1,2,3,4,5]
parents_range = [1,2,3,4,5]
ratio_range = [[1,1],[2,2],[3,4],[5,6]]
mode = "sum"

gi.set_parameters({
    'tests': 40,
    'a': 0,
    'p': 0,
    't': 1,
    'generations': 2,
    'generations_sizes': 1000,
    'traits_function': mode,
    'target': [1,1]
})

# calculate data
for parents in parents_range:
    for ratio in ratio_range:
        gi.calc_smoothed_percents(parents, ratio)
gi.calc_first_slopes(parents_range,ratio_range)

# plot
gi.initfig()
for ratio in ratio_range:
    gi.plot_first_slopes_parents(parents_range,ratio,regression_type="linear")

# save
gi.legend()
gi.title("Selection versus Parent #; 2-Gene: " + mode.upper())
gi.savefig("outputs/tmp/fig3_t2_"+mode.lower()+"_p1-5_m1000_n2.png")