import genealogy_multitraits as genealogy
import dot_creator
import genealogy_multitraits_inspector as gi
import numpy as np
import sys
import time
import file_manager

# tests, parents, generations, generations_sizes, a, p, t, traits

parents_range = [1,3,6]

gi.set_parameters({
	'tests': 10,
	'generatiaons': 2,
	'generations_sizes': 20,
	'a': 0,
	'p': 0,
	't': 1,
	'traits': [1,2,3],
	'target': [1,1,1],
	'traits_function': 'prod' # prod or sum
})

gi.calc_smoothed_percents_range(parents_range)
gi.calc_first_slopes(parents_range)

gi.initfig()

gi.plot_first_slopes_parents(parents_range,"linear")

gi.savefig("outputs/tmp/test.png")