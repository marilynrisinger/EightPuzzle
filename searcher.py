Ei#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# Marilyn Risinger




import random
from state import *

GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    
    
    def __init__(self, depth_limit):
        """constructs a new Searcher object by initializing the following 
        attributes: states, num_tested, depth_limit"""
        self.states=[]
        self.num_tested = 0
        self.depth_limit=depth_limit

    

    def add_state(self, new_state):
        """takes a single State object called new_state and adds it 
        to the Searcher‘s list of untested states"""
        self.states+=[new_state]
        
        
   
    
    def should_add(self, state):
        """takes a State object called state and returns True 
        if the called Searcher should add state to its list of 
        untested states, and False otherwise"""
        if state.creates_cycle() == True:
            return False
        elif self.depth_limit!=-1 and state.num_moves>self.depth_limit:
            return False
        elif state == GOAL_TILES:
            return False
        else:
            return True
        
    
    
    def add_states(self, new_states):
        """takes a list State objects called new_states, and 
        that processes the elements of new_states one at a time"""
        for x in new_states:
            if self.should_add(x)==True:
                self.add_state(x)
                
    
    
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    
    
    
    def find_solution(self, init_state):
        """that performs a full state-space search that begins 
        at the specified initial state init_state and ends when 
        the goal state is found or when the Searcher runs out of
        untested states"""
        self.add_state(init_state)
        while len(self.states)>0:
            s = self.next_state()
            self.num_tested+=1
            if s.board.tiles == GOAL_TILES:
                return s
            else:
                self.add_states(s.generate_successors())
        return None
    



    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s




class BFSearcher(Searcher):
    """for searcher objects that perform breadth-first search 
    (BFS) instead of random search. As discussed in lecture, BFS 
    involves always choosing one the untested states that has 
    the smallest depth"""
    def next_state(self):
        """this version of next_state should follow FIFO 
        (first-in first-out) ordering – choosing the state that 
        has been in the list the longest"""
        s = self.states[0]
        self.states.remove(s)
        return s
    



    
class DFSearcher(Searcher):
    """for searcher objects that perform depth-first search (DFS) 
    instead of random search. As discussed in lecture, DFS involves 
    always choosing one the untested states that has the largest 
    depth"""
    def next_state(self):
        """method should follow LIFO (last-in first-out) ordering 
        – choosing the state that was most recently added to the 
        list"""
        s = self.states[-1]
        self.states.remove(s)
        return s
    

        
                   


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0


    
def h1(state):
    """a hueristic function that takes the number of misplaces tiles
    and is used in priority functions to determine the priority.
    the lower the number of misplaced tiles the higher the priority."""
    return state.board.num_misplaced()




def h2(state):
    """a heuristic function that I created that adds up the values of the
    tiles misplacement. If the tile is in the correct row or column, but not
    both it adds 1 and if it is in the wrong row and column it adds 2"""
    
    return state.board.col_row_misplaced()
    
    
    


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    
    
    def __init__(self, heuristic):
        """constructs a new GreedySearcher object"""
        super().__init__(self)
        
        self.heuristic = heuristic
        self.depth_limit= -1

    
    
    def priority(self, state):
        """computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)


    

    def add_state(self, state):
        """overrides (i.e., replaces) the add_state method that is 
        inherited from Searcher. Rather than simply adding the 
        specified state to the list of untested states, the method 
        should add a sublist that is a [priority, state] pair, 
        where priority is the priority of state that is determined 
        by calling the priority method"""
        self.states+=[[self.priority(state), state]]


   
    
    def next_state(self):
        """overrides (i.e., replaces) the next_state method that 
        is inherited from Searcher. This version of next_state 
        should choose one of the states with the highest priority"""
        s = max(self.states)
        self.states.remove(s)
        return s[1]



    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s




class AStarSearcher(GreedySearcher):
    """for searcher objects that perform A* search. Like greedy s
    earch, A* is an informed search algorithm that assigns a priority
    to each state based on a heuristic function, and that selects 
    the next state based on those priorities. However, when A* 
    assigns a priority to a state, it also takes into account the 
    cost that has already been expended to get to that state (i.e. 
    the number of moves to that state)"""
    
    def priority(self,state):
        """only changing the priority state because that is the only
        difference from GrredySearcher and AStarSearcher"""
        x = self.heuristic(state) + state.num_moves
        return -1*x
    
    
    
    
    

