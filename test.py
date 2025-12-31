from Domains.TireDomain import TireDomain
from Problems.TireProblem import Tire

from Planners.ForwardPlanner import ForwardPlanner

for_planner = ForwardPlanner(Tire(TireDomain()))

print(for_planner.search())