import numpy as np
from traitsgenealogy import Genealogy
import fitnessfunctions as ff
import inspector

gen = Genealogy(
    10, # how many iterations :: int
    10, # number of members in each generation
    1, # parents each member has :: int
    [2,3], # how much each trait is worth :: [float]
    ff.PROD, # how to combine traits into fitness :: [bool] -> float
    [0,50,50,0] # relative abundancy of traits in gen0 :: [bool]
)

inspector.plotAllDistributions(gen)
# inspector.plotTargetDistribution(gen,0)

# inspector.show()