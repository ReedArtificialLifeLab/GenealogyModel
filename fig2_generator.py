import genealogy_inspector as gi
import numpy as np

tests = 10
generations = 50
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

# # calculate data
# for ratio in ratio_range:
#     gi.calc_smoothed_percents(parents,ratio,tests)

# plot
gi.initfig()
for ratio in ratio_range:
    gi.plot_percents(parents,ratio,regression=True)

# save
gi.legend()
gi.title("Growth of Dominant Trait; Single-Gene")
gi.savefig("outputs/tmp/test.png")