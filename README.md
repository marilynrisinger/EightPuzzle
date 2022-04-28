# EightPuzzle
An EighPuzzle game with different levels of A.I. players to solve the puzzle. 

To run the code use 
eight_puzzle(x , y , -1)

x = an inputted board, so the numbers 0,1,2,3,4,5,6,7,8 in a random order as a string
an example of x would be '142358607'

y = an A.I. input as a string
options for y: 
- 'random' = the tiles are randomly shuffled until a solution is found
- 'BFS' = a breadth-first search approach (chooses one of the untested states that has the smallest depth)
- 'DFS' = a depth-first search approach (chooses one of the untested states that has the largest depth
- 'GreedySearcher' = uses a heuristic function to estimate the remaining cost needed to get from a given state to the goal state
- 'AStarSearcher' = an informed search algorithm that assigns a priority to each state based on as a heuristic function and that selects the next state based on those priorities

an exammple to run the code would be
eight_puzzle('142358607', 'random', -1)
