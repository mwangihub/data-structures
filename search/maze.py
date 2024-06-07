import sys
import logging
from search.node import Node, StackFrontier

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="logs/search_algorithm.log",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    encoding="utf-8",
    level=logging.DEBUG,
)


class Maze:
    def __init__(self, filename=None, *args, **kwargs):
        """
        The __init__ function is the constructor for a class. It is called when an object of that class is created.
        The __init__ function can take any number of arguments, but it must have at least one argument (self).
        :param self: Represent the instance of the class
        :param filename: Read the maze file
        :param *args: Send a non-keyworded variable length argument list to the function
        :param **kwargs: Pass keyworded, variable-length argument list
        :return: Nothing
        """
        if not filename:
            try:
                self.file = "maze.txt"
            except:
                logger.error("Maze File NOT found! ")
                return
        else:
            self.file = filename

        with open(str(self.file)) as f:
            contents = f.read()
            if contents.count("A") != 1:
                logger.error(
                    "Maze File must have exactly one start point, Denoted by 'A' "
                )
                return
            if contents.count("B") != 1:
                logger.error(
                    "Maze File must have exactly one endpoint, Denoted by 'B' "
                )
                return
            contents = contents.splitlines()
            self.height = len(contents)
            self.width = max(len(line) for line in contents)
            self.walls = []
            for step in range(self.height):
                # For every step in height
                row = []
                for width in range(self.width):
                    try:
                        # check position of A
                        if contents[step][width] == "A":
                            self.start = [step][width]
                            row.append(False)
                        elif contents[step][width] == "B":
                            self.goal = [step][width]
                            row.append(False)
                        elif contents[step][width] == " ":
                            row.append(False)
                        else:
                            row.append(True)
                    except IndexError:
                        row.append(False)
                self.walls.append(row)

            self.solution = None

    def print(self):
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
        self.number_state_explored = 0
        start = Node(state=self.start)
        frontier = StackFrontier()
        frontier.add(start)


if __name__ == "__main__":
    try:
        maze = Maze()
    except:
        print("Error while running Maze()")
