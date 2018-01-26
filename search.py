# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

    # To solve the search problems in the question 1 through 4 a generalized search function is used. 
    # So calling the search function with its respective parameters will solve the problem.
    # Search function is at the end of 'search.py'
    # Using this approach we dont need to write similar code for all the problems.

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    return searchProblem(problem, util.Stack())

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return searchProblem(problem, util.Queue())

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return aStarSearch(problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    return searchProblem(problem, util.PriorityQueue(), heuristic)

def searchProblem(problem, fringe, heuristic=None):
    
    # visited is the array consisting the already visited node
    visited = []       
    # action is the array consisting of already taken actions by agent 0(PACMAN)
    action = []    
    #Starting state for agent 0
    start = problem.getStartState()  

    # isinstance function return true if fringe is instance of util data structures
    # for dfs and bfs stack and queue operations will performed respectively
    # for ucs and astar priority queue is used
    
    if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
        fringe.push((start, action))
    elif isinstance(fringe, util.PriorityQueue):
        fringe.push((start, action), heuristic(start, problem))

    # data structures are feed with the start state and the actions list
    # the priority in priority queue is evaluated with the help of heuristic
    # this loop executes as long as fringe has elements in it.
    while fringe: 
        if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
            node, actions = fringe.pop() 
        elif isinstance(fringe, util.PriorityQueue):
            node, actions = fringe.pop()
        
        # nodes are explored if they are not in visited[] and added to the visited[]
        # check if node is goal first
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            successors = problem.getSuccessors(node)
            for successor in successors:
                coordinate, direction, cost = successor
                newActions = actions + [direction]
                if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
                    fringe.push((coordinate, newActions))
                elif isinstance(fringe, util.PriorityQueue):
                    newCost = problem.getCostOfActions(newActions) + \
                               heuristic(coordinate, problem)
                    fringe.push((coordinate, newActions), newCost)                  

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
