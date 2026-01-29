# planning
**********************************************************************************
#Spare tire problem (ZAPAS)
(Forward planning = BFS from init to goal with a FIFO frontier queue and a visited set)

TireDomain:

Initial state

At(Flat, Axle)
At(Spare, Trunk)

***

Final state

At(Spare, Axle)
At(Flat, Ground)

***

test.py output:

['Remove(Flat,Axle)', 'Remove(Spare,Trunk)', 'PutOn(Spare,Axle)']

**********************************************************************************
#BLOCK WORLD
Constraint: only clear blocks can be moved.

(Backward planning = BFS from init to goal (regression) using a FIFO frontier queue and a visited set, reverse the sequence before returning it.)
[it's reversed so the plan can be executed from the initial state to reach the goal.] @ BackwardPlanner.py line 44

Blocks Domain:

Initial state:

On(Block3, Table)

On(Block2, Block3)

On(Block1, Block2)

Clear(Block1)

|block1|
|block2|
|block3|

***

Final state:

On(Block2, Table)

On(Block3, Block2)

On(Block1, Block3)

Clear(Block1)

|block1|
|block3|
|block2|
 
 ***

testblockworld.py output (Backward Planner):

Backward BlockDomain plan:
MoveToTable(Block1,Block2)
MoveToTable(Block2,Block3)
Move(Block3,Table,Block2)
Move(Block1,Table,Block3)

