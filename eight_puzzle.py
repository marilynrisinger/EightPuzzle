#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# Marilyn Risinger

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)

    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()





def process_file(filename, algorithm, param):
    """Function that takes a filename, algorithm and parameter and opens
    the file, obtains the digitstring from the lines of the file, 
    solves the eight puzzle for that digit string using the algorithm and
    parameter specified by the second and third inputs to the function,
    reports the number of moves in the solution and the states tested during 
    the search for a solution, then prints the total number of puzzles solved,
    the average number of moves in the solutions, average number of states
    tested"""
    file = open(filename)
    """"searcher = create_searcher(algorithm, param)"""
    solved_puzzles=0
    total_moves=0
    states_tested=0
    for line in file:
        line = line[:-1]
        init_board = Board(line)
        s = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return

        soln = None
        
        try:
            soln = searcher.find_solution(s)
        except KeyboardInterrupt:
            print('search terminated,', end='')



        if soln == None:
            print(line + ': no solution')
        else:
            print(line, ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
            states_tested+=searcher.num_tested
            solved_puzzles+=1
            total_moves+=int(soln.num_moves)
    
    if solved_puzzles==0:
        print('')
        print('solved', solved_puzzles, 'puzzles')
        
    else:
        print('')
        print('solved', solved_puzzles, 'puzzles')
        print('averages:', total_moves/solved_puzzles, 'moves,', states_tested/solved_puzzles, 'states tested')
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

