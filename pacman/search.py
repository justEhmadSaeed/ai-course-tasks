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
    return [s, s, w, s, w, w, s, w]


def mediumClassicSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    return [w, w, w, n, n]


def mediumMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    return [w, w, w, w, w, w, w, w, w,
            s, s, e, e, s, s, s,
            w, w, w, n, w, w, w, w,
            s, s, s, e, e, e, e, e, e, e,
            s, s, s, s, s, s, s,
            w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w,
            s, w, w, w, w, w, w, w, w, w
            ]


def bigMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    return [n, n, w, w, w, w, n, n, w, w, s, s,
            w, w, w, w, w, w, w, w, w, w, w, w, w, w, n, n, e, e, n, n, w, w, n, n, n, n, n, n,
            e, e, e, e, e, e, s, s, e, e, n, n, e, e, e, e, n, n, e, e, s, s, e, e,
            n, n, n, n, n, n, e, e, e, e, n, n, n, n, n, n, n, n, n, n, w, w, s, s, w, w, w, w,
            s, s, s, s, s, s, w, w, s, s, s, s, w, w, n, n, w, w, w, w, w, w, w, w, w, w, w, w,
            n, n, e, e, n, n, n, n, n, n, e, e, e, e, e, e, n, n, n, n, n, n, n, n, w, w, w, w, w, w,
            s, s, w, w, w, w, s, s, s, s, e, e, s, s, w, w, w, w, w, w, w, w, w, w,
            s, s, s, s, s, s, s, s, s, s, e, e, s, s, s, s, w, w, s, s, s, s, e, e,
            s, s, w, w, s, s, s, s, w, w, s, s
            ]


def DFS(problem):
    '''
    Challenge 01: Increase the maxIteration to 20,30 and 40 and see the behavior of pacman. If pacman do not die out, at
    some stage, it will be stuck in loop and cannot move forward. Write down the reason why he is getting into the loop and
    identify the part of the code which need to be modified.

    Answer:
    Whenever problem.getSuccessors(currentState) is called, it returns a list of
    possible states where the pacman can move to. This list is sorted in the following
    order [North, South, East, West]. And the given code always choose the first child
    of the successors. Which means the available highest ordered child is chosen.

    At the 13rd iteration, the successors are South & West and due to higher order of South,
    the program chooses South. At the next iteration, the successors are North & South.
    And program chooses North due to its order higher than South.

    But at the next iteration, the successors are again South and West and it chooses South.
    This loop keeps choosing South among South & West, which leads to the successors of 
    North & South. And the selection of North takes the program again to the successors of
    South and West, so the pacman gets stuck in a loop.

    The part where the program always chooses first child has to be modified, because due to sorting
    of successors, the highest order child will always be selected, no matter what.
    '''
    currentState = problem.getStartState()
    print currentState
    actions = []
    maxIteration = 0
    previousState = currentState
    while (maxIteration <= 20):
        children = problem.getSuccessors(currentState)
        print children
        if previousState == children[0][0]:
            firstChild = children[1]
        else:
            firstChild = children[0]

        previousState = currentState
        actions.append(getActionFromTriplet(firstChild))
        firstChildState = firstChild[0]
        currentState = firstChildState
        maxIteration = maxIteration + 1

    print actions
    return actions


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
    currentState = problem.getStartState()

    frontier = util.Stack()
    frontier.push((currentState, []))

    explored = set()
    explored.add(currentState)

    while not frontier.isEmpty():
        Directions = frontier.pop()
        state = Directions[0]
        actions = Directions[1]

        currentState = problem.getSuccessors(state)

        for child in currentState:
            state = child[0]
            direction = child[1]

            if state not in explored:
                if problem.isGoalState(state):
                    actions += [direction]
                    print actions
                    return actions
                else:
                    frontier.push((state, actions + [direction]))
                    explored.add(state)

    return []
    util.raiseNotDefined()


def getActionFromTriplet(triple):
    return triple[1]


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()

    frontier = util.Queue()
    frontier.push((currentState, []))

    explored = set()
    explored.add(currentState)

    while not frontier.isEmpty():
        Directions = frontier.pop()
        state = Directions[0]
        actions = Directions[1]

        currentState = problem.getSuccessors(state)

        for child in currentState:
            state = child[0]
            direction = child[1]

            if state not in explored:
                if problem.isGoalState(state):
                    actions += [direction]
                    print actions
                    return actions
                else:
                    frontier.push((state, actions + [direction]))
                    explored.add(state)

    return []
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
