import genealogy, genealogy_multitraits, csv_creator, dot_creator

# parameters

generations       = 30
generations_size  = 10
parents_range     = [1,1,2,4]
age_factor_range  = [0,0,0,0]
trait_ratio_range = [1,2,2,2]

# definition

def trial(parents,age_factor,trait_ratio):
    genealogy.init_genealogy()

    name = "trial_P=" + str(parents) + "_A=" + str(age_factor) + "_R=" + str(trait_ratio)
    
    gen_data = genealogy.make_genealogy(
        name                      = name,
        generations               = generations,
        generation_sizes_function = lambda x: generations_size,
        parents                   = parents,
        balanced                  = True,
        trait_factor              = 1,
        age_factor                = age_factor,
        popular_factor            = 0,
        trait_weights             = [trait_ratio,1] )
    
    dot_creator.create_dot(gen_data,pdf=True)

# running

# trial(1,0,2)

[ trial(parents,age_factor,trait_ratio)
    for parents in parents_range
    for age_factor in age_factor_range
    for trait_ratio in trait_ratio_range ]

# for parents in parents_range:
#     for age_factor in age_factor_range:
#         for trait_ratio in trait_ratio_range:
#             trial(parents,age_factor,trait_ratio)