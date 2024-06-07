import sys

import sys
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="logs/search_algorithm.log",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    encoding="utf-8",
    level=logging.DEBUG,
)


class Node:

    def __init__(self, parent=None, state=None, action=None) -> None:
        """
        The __init__ function is the constructor for a class. It is called when an object of that class
        is created, and it sets up the attributes of that object. In this case, we are creating a node
        object with three attributes: parent (the parent node), state (the current state), and action
        (the action taken to get from the parent to this node). The __cost__ attribute keeps track of how many nodes have been expanded.

        :param self: Represent the instance of the class
        :param parent: Keep track of the parent node
        :param state: Store the current state of the node
        :param action: Keep track of the action that was used to get from the parent node to this node
        :return: None
        """
        cost = 1
        self.parent = parent
        self.state = state
        self.action = action
        self.__cost__ = cost + 1


class StackFrontier:

    def __init__(self) -> None:
        """
        The __init__ function is called when the class is instantiated.
        It initializes the stack_frontier to an empty list.
        :param self: Represent the instance of the class
        :return: None
        """
        self.stack_frontier = []

    def add(self, node):
        """
        The add function adds a node to the stack frontier.
            Args:
                node (Node): The Node object that is being added to the stack frontier.
            Returns:
                None
        :param self: Represent the instance of the class
        :param node: Add a node to the stack_frontier
        :return: The length of the stack_frontier list
        """
        return self.stack_frontier.append(node)

    def contains_state(self, state):
        """
        The contains_state function checks to see if the state is in the stack_frontier.
            If it is, then it returns True. Otherwise, it returns False.

        :param self: Represent the instance of the object itself
        :param state: Check if the state is in the stack_frontier
        :return: A boolean value
        """
        return any(node.state == state for node in self.stack_frontier)

    def remove(self):
        """
        The remove function removes the last element of the stack frontier.
            It returns a node that is removed from the stack frontier.

        :param self: Access the attributes and methods of a class
        :return: The last element in the stack
        """
        if self.is_empty():
            print("\n Stack Frontier is Empty\n")
            return
        node = self.stack_frontier[-1]
        self.stack_frontier = self.stack_frontier[:-1]
        return node

    def is_empty(self):
        """
        The is_empty function checks to see if the stack is empty.
            If it is, then it returns True. Otherwise, it returns False.

        :param self: Refer to the object itself
        :return: True if the stack is empty and false otherwise
        """
        return len(self.stack_frontier) == 0


class QueuedStackFrontier(StackFrontier):

    def remove(self):
        """
        The remove function removes the first element in the queue.
            It does this by slicing off the first element of stack_frontier, and then returning that node.
        :param self: Access the attributes of the class
        :return: The node at the front of the queue
        """
        if self.is_empty():
            print("\nQueue Stack is empty\n")
            return
        node = self.stack_frontier[0]
        self.stack_frontier = self.stack_frontier[1:]
        return node


class Maze:

    def __init__(self, filename="maze.txt"):

        # Read file and set height and width of maze
        """
        The __init__ function is called when the class is instantiated.
        It sets up the maze by reading in a file and setting up some variables.


        :param self: Represent the instance of the class
        :param filename: Read the maze from a file
        :return: Nothing
        """
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        """
        The print function prints the maze with walls, start and goal.
        If a solution is found, it will also print the path from start to goal.

        :param self: Represent the instance of the class
        :return: A string representation of the object
        """
        if not self.goal and self.start:
            logger.critical("The program missed goal i.e B and start i.e A")
            print("\n Program exit with error \n")
            return

        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("▮", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        """
        The neighbors function returns a list of tuples containing the valid actions and their corresponding neighbors.
        The candidates are all possible actions, but not all of them will be valid in the current state.
        For example, if we're at (0, 0), then &quot;up&quot; is not a valid action because it would take us outside the grid.
        We can use try/except to filter out invalid states:

        :param self: Represent the object itself
        :param state: Determine the current position of the agent
        :return: A list of tuples
        """
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]
        results = []
        for action, (row, col) in candidates:
            try:
                if not self.walls[r][c]:
                    results.append((action, (row, col)))
            except IndexError:
                continue
            return results

    def solve(self):
        """
        The solve function is the main function of this module. It takes in a Maze object and returns a tuple containing two lists:
            1) A list of actions that can be taken to solve the maze, where each action is one of 'N', 'S', 'W', or 'L'.
            2) A list of (x, y) tuples representing the coordinates visited by taking those actions from start to finish.

        :param self: Access the attributes of the class
        :return: A tuple of actions and states explored
        """
        self.number_state_explored = 0
        start = Node(state=self.start)
        frontier = StackFrontier()
        frontier.add(start)
        self.explored = set()
        while True:
            if frontier.is_empty():
                logger.warning("No solution found!")
                return
            node = frontier.remove()
            self.number_state_explored += 1
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            self.explored.add(node.state)
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)


if __name__ == "__main__":
    maze = Maze()
    maze.print()
