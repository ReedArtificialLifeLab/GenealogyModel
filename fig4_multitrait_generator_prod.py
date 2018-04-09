import genealogy_multitraits_inspector as gi
import numpy as np

# parents_range = [1,10,20,30,40,50,60,70,80,90,100]
parents_range = [ i for i in range(1,11) ]
ratio = [4,32]
ratio_range = [ratio]
tests = 100

mode = "prod"

gi.set_parameters({
    'tests': tests,
    'a': 0,
    'p': 0,
    't': 1,
    'generations': 2,
    'generations_sizes': 100,
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
    gi.plot_first_slopes_parents(parents_range,ratio,regression_type="quadratic")

# save
gi.legend()
gi.title("Selection vs Parent #; 2-Character; "+mode.capitalize())
gi.savefig(
    "outputs/tmp/fig4_t2"+
    "_mode"+mode.capitalize()+
    "_p"+str(parents_range[0])+"-"+str(parents_range[1])+
    "_m100_n2_r"+str(ratio[0])+"-"+str(ratio[1])+
    ".png")
