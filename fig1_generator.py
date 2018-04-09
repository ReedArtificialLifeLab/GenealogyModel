import genealogy, genealogy_multitraits, csv_creator, dot_creator

p = 4
v = 1

genealogy.init_genealogy()
gen_data = genealogy.make_genealogy(
    name                      = "p"+str(p)+"_v"+str(v),
    generations               = 30,
    generation_sizes_function = lambda x: 10,
    parents                   = p,
    balanced                  = True,
    trait_factor              = 1,
    age_factor                = 0,
    popular_factor            = 0,
    trait_weights             = [v,1] )

dot_creator.create_dot(gen_data,pdf=True)