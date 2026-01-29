from Domains.TireDomain import TireDomain
from Problems.TireProblem import Tire

"""
For Tire domain,
Init state:
At(Flat, Axle)
At(Spare, Trunk)

Goal State:
At(Spare, Axle)
At(Flat, Ground)
"""

from Planners.ForwardPlanner import ForwardPlanner


for_planner = ForwardPlanner(Tire(TireDomain()))

print(for_planner.search())

#output = ['Remove(Flat,Axle)', 'Remove(Spare,Trunk)', 'PutOn(Spare,Axle)']

