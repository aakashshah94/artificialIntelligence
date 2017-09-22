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
import sys

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
    # initial print statements to understand the problem structure
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # if start is the goal state do nothing and return"""
    if problem.isGoalState(problem.getStartState()):
        return "nothing"
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # getting the data structure
    stack = util.Stack()
    #add the initial node with cost 0 and mark it as start
    stack.push([(problem.getStartState(), "start", 0)])
    # a list of visited nodes
    visited = []
    #dfs logic
    #get the last node added to the stack
    while not stack.isEmpty():
        #getting the last node with complete path and cost
        node_plus_path = stack.pop()
        # getting the last node reached in the path
        last_node = node_plus_path[len(node_plus_path)-1][0]
        # executed when goal is reached
        if problem.isGoalState(last_node):
            answer = []
            # getting the directions or actions only in answer and ignoring the start state
            for i in range(1, len(node_plus_path)):
                answer.append(node_plus_path[i][1])
            return answer
        # executed when goal not reached
        if last_node not in visited:
            #if not already visited visit the node
            visited.append(last_node)
            # generate all successors and add the path to those successors,right is explored each time
            for successor in problem.getSuccessors(last_node):
                if successor[0] not in visited:
                    # deep copying the path
                    tempPath = node_plus_path[:]
                    # adding this node to the path
                    tempPath.append(successor)
                    #always adding complete path to that node
                    stack.push(tempPath)
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    """if start is the goal state do nothing and return"""
    if problem.isGoalState(problem.getStartState()):
        return "nothing"
    # getting the queue data structure from util
    queue=util.Queue()
    #a list of visited nodes
    visited=[]
    #adding the initial node with cost 0 and marked as start
    queue.push([(problem.getStartState(),"start",0)])
    while not queue.isEmpty():
        #gettig the last node which has last node co-ordinate and complete path
        node_plus_path=queue.pop()
        #taking only the last node
        last_node = node_plus_path[len(node_plus_path)-1]
        #co-ordinates of last node
        last_node = last_node[0]
        # executed when goal is reached
        if problem.isGoalState(last_node):
            answer = []
            # getting the directions or actions only in answer and ignoring the start state
            for i in range(1, len(node_plus_path)):
                answer.append(node_plus_path[i][1])
            return answer
        # executed when goal not reached
        if last_node not in visited:
            visited.append(last_node)
            # generate all successors and add the path to those successors,right is explored each time
            for successor in problem.getSuccessors(last_node):
                if successor[0] not in visited:
                    # deep copying the path
                    tempPath = node_plus_path[:]
                    # adding this node to the path
                    tempPath.append(successor)
                    queue.push(tempPath)
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    if problem.isGoalState(problem.getStartState()):
        return "nothing"
    # getting the Priorityqueue data structure from util
    queue=util.PriorityQueue()
    # a list of visited nodes
    visited=[]
      #adding the initial node with cost 0 and marked as start
    queue.push([(problem.getStartState(), "Start" , 0)],0)
    while not queue.isEmpty():
        #gettig the last node which has last node co-ordinate and complete path
      
        node_plus_path=queue.pop()
        last_node = node_plus_path[len(node_plus_path)-1]
        last_cost=0
        #calculating the total cost of reaching this node
        for x in node_plus_path:
            last_cost+=x[2]
        # executed when goal is reached
        if problem.isGoalState(last_node[0]):
            answer = []
            # getting the directions or actions only in answer and ignoring the start state
            for i in range(1, len(node_plus_path)):
                answer.append(node_plus_path[i][1])
            return answer
        # executed when goal not reached
        if last_node[0] not in visited:
            visited.append(last_node[0])
            # generate all successors and add the path to those successors,right is explored each time

            for successor in problem.getSuccessors(last_node[0]):
                if successor[0] not in visited:
                    # deep copying the path
                    tempPath = node_plus_path[:]
                    # adding this node to the path
                    tempPath.append(successor)
                    #adding the node to the queue along with the complete cost to 
                    #reach the node and its oown cost added
                    queue.push(tempPath,last_cost+successor[2])
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    if problem.isGoalState(problem.getStartState()):
        return "nothing"
    # getting the Priorityqueue data structure from util
    queue=util.PriorityQueue()
    # a list of visited nodes
    visited=[]
    #adding the initial node with path cost 0 and marked as start
    queue.push([(problem.getStartState(), "Start" , 0)],heuristic(problem.getStartState(),problem))
    while not queue.isEmpty():
        #gettig the last node which has last node co-ordinate and complete path
      
        node_plus_path=queue.pop()
        last_node = node_plus_path[len(node_plus_path)-1]
        last_cost=0
        #calculating complete cost to reach the node
        for x in node_plus_path:
            last_cost+=x[2]
        # executed when goal is reached
        if problem.isGoalState(last_node[0]):
            answer = []
            # getting the directions or actions only in answer and ignoring the start state
            for i in range(1, len(node_plus_path)):
                answer.append(node_plus_path[i][1])
            return answer
        # executed when goal not reached
        if last_node[0] not in visited:
            visited.append(last_node[0])
            # generate all successors and add the path to those successors,right is explored each time

            for successor in problem.getSuccessors(last_node[0]):
                if successor[0] not in visited:
                    # deep copying the path
                    tempPath = node_plus_path[:]
                    # adding this node to the path
                    tempPath.append(successor)
                    #adding the node to the queue along with the complete cost
                    #to reach the node added with its own cost
                    queue.push(tempPath,heuristic(successor[0],problem)+last_cost+successor[2])
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
