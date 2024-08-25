
import util


class SearchProblem:
  
    def getStartState(self):
        
        util.raiseNotDefined()

    def isGoalState(self, state):
       
        util.raiseNotDefined()

    def getSuccessors(self, state):
       
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
       
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):


    from util import Stack

    # Creates an empty Stack.
    open_list = Stack()

    visited_list = []
    path = []
    action_cost = 0  # Cost of each movement.

    start_position = problem.getStartState()

    # Pushes the start position to the stack.
    open_list.push((start_position, path, action_cost))

    while not open_list.isEmpty():

        current_node = open_list.pop()
        position = current_node[0]
        path = current_node[1]

        # Pushes the current position to the visited list if it is not visited.
        if position not in visited_list:
            visited_list.append(position)
            # print("visited",visited_list)

        # Returns the final path if the current position is goal.
        if problem.isGoalState(position):
            print("Path found:", path)
            return path

        # Gets successors of the current node.
        successors = problem.getSuccessors(position)

        # Pushes the current node's successors to the stack if they are not visited.
        for item in successors:
            if item[0] not in visited_list:

                new_position = item[0]
                new_path = path + [item[1]]
                open_list.push((new_position, new_path, item[2]))

    util.raiseNotDefined()


def breadthFirstSearch(problem):
 
    from util import Queue

    # Creates an empty Queue.
    open_list = Queue()

    visited_list = []
    path = []
    action_cost = 0  # Cost of each movement.

    start_position = problem.getStartState()

    # Pushes the start position to the Queue.
    open_list.push((start_position, path, action_cost))

    while not open_list.isEmpty():

        current_node = open_list.pop()
        position = current_node[0]
        path = current_node[1]

        # Pushes the current position to the visited list if it is not visited.
        if position not in visited_list:
            visited_list.append(position)

        # Returns the final path if the current position is goal.
        if problem.isGoalState(position):
            print("Path found:", path)
            return path

        # Gets successors of the current node.
        successors = problem.getSuccessors(position)

        # Pushes the current node's successors to the Queue if they are not visited.
        # We check both visited and open list.
        for item in successors:
            if item[0] not in visited_list and item[0] not in (node[0] for node in open_list.list):

                new_position = item[0]
                new_path = path + [item[1]]
                open_list.push((new_position, new_path, item[2]))


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch

# python3 pacman.py -l bigMaze -z .5 -p SearchAgent  
# python3 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5