import genealogy_inspector as gi
import numpy as np

tests = 100
generations = 2
generations_sizes = 100
a = 0
p = 0
t = 1

parents_range = [1,10,20,30,40,50,60,70,80,90,100]
ratio_range = [4]

gi.set_parameters({
    'a': a,
    'p': p,
    't': t,
    'generations': generations,
    'generations_sizes': generations_sizes,
    'balanced': True
    # 'initial_counts': [1,generations_sizes]
})

# calculate data
# gi.calc_smoothed_percents_range(parents_range,ratio_range,tests)
# gi.calc_first_slopes(parents_range,ratio_range)

# plot
gi.initfig()
for ratio in ratio_range:
    gi.plot_first_slopes_parents(parents_range,ratio,regression_type="quadratic")

# save
gi.title("X' versus Parents; Single-Gene")
# gi.legend()
gi.savefig("outputs/tmp/fig4_t1_p1-100_m100_n2.png")