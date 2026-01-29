from Domains.BlockWorld import BlockDomain
from Problems.block import Block
from Planners.BackwardPlanner import BackwardPlanner


domain = BlockDomain(3)
problem = Block(domain)

planner = BackwardPlanner(problem)
plan = planner.search()

print("Backward BlockDomain plan:")
for step in plan:
    print(step)
    
"""""
output:
Backward BlockDomain plan:
MoveToTable(Block1,Block2)
MoveToTable(Block2,Block3)
Move(Block3,Table,Block2)
Move(Block1,Table,Block3)
"""