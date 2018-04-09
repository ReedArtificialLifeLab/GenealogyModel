import genealogy_multitraits_inspector as gi
import numpy as np

parents = 1
ratio_range = [[1,1], [2,2], [2,3], [5,6]]

gi.set_parameters({
    'tests': 5,
    'generatiaons': 15,
    'generations_sizes': 100,
    'a': 0,
    'p': 0,
    't': 1,
    'target': [1,1],
    'traits_function': 'prod' # prod or sum
})

# calculate data
for ratio in ratio_range:
    gi.calc_smoothed_percents(parents,ratio)

# plot
gi.initfig()
for ratio in ratio_range:
    gi.plot_percents(parents,ratio,regression=True)

# save
gi.legend()
gi.title("Growth of Dominant Trait; 2-Gene; PROD")
gi.savefig("outputs/tmp/fig2_t2_prod_n15_m100.png")