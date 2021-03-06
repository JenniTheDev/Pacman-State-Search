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

def depthFirstSearch(problem):
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # deepest nodes first
    # Have we reached the goal? base case 
    # has goal been reached?
    # get start state 
    # explore states in order
    # keep track of the order
    # create stack to hold states
    # push the states on the stack
    # get next state to explore
    # save actions to get to that point
    # next state is current state
    # if not goal, continue 
    
    #Start
    currentNode = problem.getStartState()
    #Nodes we have seen
    seen = []
    #path
    pathFromStart = []
    #stack
    stack = util.Stack()

    #if we are at our goal already, return
    if problem.isGoalState(currentNode):
        return []
    #initialize with the starting state
    stack.push((problem.getStartState(), pathFromStart))
    seen.append(problem.getStartState())
    
    #DFS
    while not stack.isEmpty():
        #base case
         if problem.isGoalState(currentNode):
            break
         nextNode, pathFromStart = stack.pop()
         if nextNode not in seen:
            seen.append(nextNode)
        
         sucessors = problem.getSuccessors(nextNode)
         for node in sucessors:  
             if not node[0] in seen:
                 direction = node[1]
                 stack.push((node[0], pathFromStart + [direction]))
                 currentNode = node[0]
                    #seen.append(node[0])
                    #stack.push((node[1], pathFromStart + [node[1]]))
                    #currentNode = node[0]
              
    pathFromStart.append(direction)
    return pathFromStart
   
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
        # if goal, return solution
        #   seen queue with node as only element
        #   unseen nodes - empty
               # for each action in problem (state node) do
                  #  child - child  (problem node action)
                    #    if child is not seen or unseen
                           # if problem goal test then return solution
                             #add child to see
     
    # From First project
    #startState = problem.getStartState()
    #visited = set()
    #queue = util.Queue()
    #queue.push((startState, ()))

    #while not queue.isEmpty():
    #    currentNode = queue.pop()
    #    currentState = currentNode[0]
    #    currentPlan = currentNode[1]
    #    if problem.isGoalState(currentState):
    #        return list(currentPlan)
    #    if not currentState in visited:
    #        visited.add(currentState)
    #        paths = problem.getSuccessors(currentState)
    #        for path in paths:
    #            newPlan = list(currentPlan)
    #            newPlan.append(path[1])
    #            nextNode = (path[0], tuple(newPlan))
    #            if not path[0] in visited:
    #                queue.push(nextNode)

    # 2nd project fixed to make sure corners work
    if problem.isGoalState(problem.getStartState()):
        return []

    queue = util.Queue()
    queue.push((problem.getStartState(),[]))
    visited = []

    while 1:
        if queue.isEmpty():
            return []
        node,actions = queue.pop()
        visited.append(node)

        for successor in problem.getSuccessors(node):
            path = actions + [successor[1]]
            if ((successor[0] not in visited) and (successor[0] not in [x for x,_ in queue.list])):
                if problem.isGoalState(successor[0]):
                    return path
                queue.push((successor[0],path))


   
   # util.raiseNotDefined()

def uniformCostSearch(problem):
    """ Ignore for this project """
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """ Ignore for this project """
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Proj 2"""
    # Open - set of nodes to be evaluated
    """Search the node that has the lowest combined cost and heuristic first."""
    closed = []  # to keep list of visited nodes - already evaluated
    open = util.PriorityQueue() # Open - set of nodes to be evaluated
    open.push([(problem.getStartState(), "Start", 0)], 0)
    # loop
    while not open.isEmpty():
    # current = node in Open with lowest f_cost
        sPath = open.pop()
        s = sPath[-1]

        if problem.isGoalState(s[0]):
         
            ansPath = []
            for p in sPath:
                ansPath.append(p[1])
            return ansPath[1:]

        if s[0] not in closed:
            closed.append(s[0])

            for child in problem.getSuccessors(s[0]):
                if child[0] not in closed or open:
                    childPath = sPath + []
                    childNew = (child[0], child[1], child[2] + s[2])
                    childPath.append(childNew)
                    open.push(childPath, childNew[2] + + heuristic(child[0], problem))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
