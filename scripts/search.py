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


##############################################################################
### User defined functions ###################################################
##############################################################################

# Get course between two points
def getCourse(start, end):
    from game import Directions

    [dx, dy] = [end[0] - start[0], end[1] - start[1]]
    direction = None

    if dy == 0 and dx > 0:
        direction = Directions.EAST
    elif dy == 0 and dx < 0:
        direction = Directions.WEST
    elif dx == 0 and dy > 0:
        direction = Directions.NORTH
    elif dx == 0 and dy < 0:
        direction = Directions.SOUTH

    return direction

# Recursive depthFirstSearch
def recursiveDFS(start, visited, stack_directions, problem):
    # If we've achieved goal
    if start == problem.goal:
        return True

    # Mark current vertex as visited
    visited.append(start)
    # Get neighbours of current vertex
    neighbours = problem.getSuccessors(start)
    for nb in neighbours:
        if nb[0] not in visited:
            if recursiveDFS(nb[0], visited, stack_directions, problem) == True:
                stack_directions.push(nb[1])
                return True
    return False

# Visualize all visited points
def showVisitedPoints(visited):
    import __main__
    __main__.__dict__['_display'].drawExpandedCells(visited)

# Reconstruct path from start to goal using list of visited points
def reconstructPath(visited, problem):
    start = problem.getStartState()
    [path_points, neighbours, last] = [[],[], None]
    for elem in visited[::-1]:
        if start in neighbours:
            path_points.append(start)
            break
        if elem in neighbours or neighbours == []:
                last = elem
                path_points.append(last)
                neighbours = [x[0] for x in problem.getSuccessors(last)]

    # Invert list to get points from start to goal
    path_points = path_points[::-1]
    return path_points

# Convert array of points to the pacman's list of rules (e.g. 'North', 'West', etc.)
def getRoute(path_points, problem):
    route = []
    start = path_points[0]
    for pt in path_points[1:]:
        course = getCourse(start, pt)
        start = pt
        route.append(course)
    return route

# Build path from goal to start
def buildPath(goal, explored):
    node = explored[goal]
    path_points = [goal]
    while not node['prev'] == None:
        path_points.append(node['prev'])
        node = explored[node['prev']]
    path_points = path_points[::-1]
    return path_points

##############################################################################
##############################################################################
##############################################################################


def depthFirstSearch(problem, recursive = True):
    # Search the deepest nodes in the search tree first.

    # List of visited vertices
    visited = []
    # Start point
    start = problem.getStartState()

    # Route for pacman
    route = []

    # Two implementations of dfs
    if recursive:
        # Movements that will lead pacman from goal to start
        stack_directions = util.Stack()

        # Get path to goal
        recursiveDFS(start, visited, stack_directions, problem)

        # Invert path to get movements from start to goal
        route = stack_directions.list[::-1]
    else:
        stack = util.Stack()
        stack.push(start)
        while not stack.isEmpty():
            vertex = stack.pop()
            visited.append(vertex)
            if vertex == problem.goal:
                break
            neighbours = problem.getSuccessors(vertex)
            for nb in neighbours:
                if nb[0] not in visited:
                    stack.push(nb[0])

        path_points = reconstructPath(visited, problem)
        route = getRoute(path_points, problem)

    # Visualize all visited points
    showVisitedPoints(visited)

    return route

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    queue = util.Queue()
    visited = []
    queue.push(problem.getStartState())

    while not queue.isEmpty():
        vertex = queue.pop()
        visited.append(vertex)
        if vertex == problem.goal:
            break
        neighbours = problem.getSuccessors(vertex)
        for nb in neighbours:
            if nb[0] not in visited:
                queue.push(nb[0])

    # Reconstruct path to goal
    path_points = reconstructPath(visited, problem)
    path = getRoute(path_points, problem)

    # Show visited points
    showVisitedPoints(visited)

    return path

# def astarUcsGeneralization(problem, heuristic=nullHeuristic)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Uniform cost search is just a special case of A* search
    # when heuristics always equals to 0
    return aStarSearch(problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    path_points = []
    start = problem.getStartState()
    reachable = util.PriorityQueue()
    start_cost = heuristic(start, problem)
    reachable.push(start, start_cost)
    # List of explored nodes
    explored = {}
    # Remember paths to reachable nodes
    prev_nodes = { start: {'prev':None, 'cost':0} }
    while not reachable.isEmpty():
        # Get next vertex
        current = reachable.pop()
        # Add node to explored
        explored[current] = prev_nodes[current]
        # Stop if we've reached the goal
        if current == problem.goal:
            break
        # Get neighbours
        neighbours = problem.getSuccessors(current)
        for nb in neighbours:
            # Calculate cost to the adjacent node
            cost_from = prev_nodes[current]['cost'] + nb[2]
            # if adjacent node is not explored
            if nb[0] not in explored.keys():
                # Calculate cost through this vertex to goal
                cost_to = heuristic(nb[0], problem)
                full_cost = cost_from + cost_to
                # Add vertex to reachable list and update its cost
                reachable.update(nb[0], full_cost)
                # Remember path to vertex
                prev_nodes[nb[0]] = {'prev':current, 'cost': cost_from}
            elif explored[nb[0]]['cost'] > cost_from:
                # Update path to known vertex if the path is more beneficial
                explored[nb[0]] = {'prev':current, 'cost': cost_from}
                prev_nodes[nb[0]] = {'prev':current, 'cost': cost_from}
    # Reconstruct path to goal
    path_points = buildPath(problem.goal, explored)
    path = getRoute(path_points, problem)
    # Show visited points
    showVisitedPoints(explored)
    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
