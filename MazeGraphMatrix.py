import WeightedGraphNode

import botCode.robomodules


class MazeGraphMatrix:

    I = 'wall'
    o = 'pellet'
    (n, e) = ('empty space', 'empty space')
    O = 'power pellet'

    grid = [[I, I, I, I, I, I, I, I, I, I, I, I, e, e, e, e, e, e, e, e, e, I, I, I, I, I, I, I, I, I, I],  # 0
            [I, o, o, o, o, I, I, O, o, o, o, I, e, e, e, e, e, e, e, e, e, I, o, o, o, o, o, O, o, o, I],
            [I, o, I, I, o, I, I, o, I, I, o, I, e, e, e, e, e, e, e, e, e, I, o, I, I, o, I, I, I, o, I],
            [I, o, I, I, o, o, o, o, I, I, o, I, e, e, e, e, e, e, e, e, e, I, o, I, I, o, I, e, I, o, I],
            [I, o, I, I, o, I, I, I, I, I, o, I, e, e, e, e, e, e, e, e, e, I, o, I, I, o, I, e, I, o, I],
            [I, o, I, I, o, I, I, I, I, I, o, I, I, I, I, I, I, I, I, I, I, I, o, I, I, o, I, I, I, o, I],  # 5
            [I, o, I, I, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, I],
            [I, o, I, I, I, I, I, o, I, I, o, I, I, I, I, I, e, I, I, I, I, I, I, I, I, o, I, I, I, o, I],
            [I, o, I, I, I, I, I, o, I, I, o, I, I, I, I, I, e, I, I, I, I, I, I, I, I, o, I, e, I, o, I],
            [I, o, I, I, o, o, o, o, I, I, o, e, e, e, e, e, e, e, e, e, I, I, o, o, o, o, I, e, I, o, I],
            [I, o, I, I, o, I, I, o, I, I, o, I, I, e, I, I, I, I, I, e, I, I, o, I, I, o, I, e, I, o, I],  # 10
            [I, o, I, I, o, I, I, o, I, I, o, I, I, e, I, n, n, n, I, e, I, I, o, I, I, o, I, I, I, o, I],
            [I, o, o, o, o, I, I, o, o, o, o, I, I, e, I, n, n, n, I, e, e, e, o, I, I, o, o, o, o, o, I],
            [I, o, I, I, I, I, I, e, I, I, I, I, I, e, I, n, n, n, n, e, I, I, I, I, I, o, I, I, I, I, I],
            [I, o, I, I, I, I, I, e, I, I, I, I, I, e, I, n, n, n, n, e, I, I, I, I, I, o, I, I, I, I, I],
            [I, o, o, o, o, I, I, o, o, o, o, I, I, e, I, n, n, n, I, e, e, e, o, I, I, o, o, o, o, o, I],  # 15
            [I, o, I, I, o, I, I, o, I, I, o, I, I, e, I, n, n, n, I, e, I, I, o, I, I, o, I, I, I, o, I],
            [I, o, I, I, o, I, I, o, I, I, o, I, I, e, I, I, I, I, I, e, I, I, o, I, I, o, I, e, I, o, I],
            [I, o, I, I, o, o, o, o, I, I, o, e, e, e, e, e, e, e, e, e, I, I, o, o, o, o, I, e, I, o, I],
            [I, o, I, I, I, I, I, o, I, I, o, I, I, I, I, I, e, I, I, I, I, I, I, I, I, o, I, e, I, o, I],
            [I, o, I, I, I, I, I, o, I, I, o, I, I, I, I, I, e, I, I, I, I, I, I, I, I, o, I, I, I, o, I],  # 20
            [I, o, I, I, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, I],
            [I, o, I, I, o, I, I, I, I, I, o, I, I, I, I, I, I, I, I, I, I, I, o, I, I, o, I, I, I, o, I],
            [I, o, I, I, o, I, I, I, I, I, o, I, e, e, e, e, e, e, e, e, e, I, o, I, I, o, I, e, I, o, I],
            [I, o, I, I, o, o, o, o, I, I, o, I, e, e, e, e, e, e, e, e, e, I, o, I, I, o, I, e, I, o, I],
            [I, o, I, I, o, I, I, o, I, I, o, I, e, e, e, e, e, e, e, e, e, I, o, I, I, o, I, I, I, o, I],  # 25
            [I, o, o, o, o, I, I, O, o, o, o, I, e, e, e, e, e, e, e, e, e, I, o, o, o, o, o, O, o, o, I],
            [I, I, I, I, I, I, I, I, I, I, I, I, e, e, e, e, e, e, e, e, e, I, I, I, I, I, I, I, I, I, I]]
    #        |         |         |         |         |         |         |
    #        0         5        10        15       20         25       30

    matrix = [[]]

    # in iteration, start at 1 because edges are borders

    def __init__(self):
        for y in range(1, len(self.grid) - 1):
            for x in range(1, len(self.grid[0]) - 1):
                # iterate through the maze
                if self.grid[y][x] == 'pellet' or self.grid[y][x] == 'power pellet':
                    # add pellet space to graph matrix
                    if self.grid[y][x] == 'pellet':
                        self.matrix[y][x] = WeightedGraphNode.WeightedGraphNode(-1, x, y)
                    else:
                        # power pellets have a very high weight so we avoid them until we specifically seek them out
                        self.matrix[y][x] = WeightedGraphNode.WeightedGraphNode(100000, x, y)

                    # iterate down-right; add double edges up-left of current space

                    # link up
                    if self.grid[y-1][x] == 'pellet' or self.grid[y-1][x] == 'power pellet':
                        self.matrix[y][x].neighbors.add_edge(self.matrix[y-1][x])

                    # link left
                    if self.grid[y][x-1] == 'pellet' or self.grid[y][x-1] == 'power pellet':
                        self.matrix[y][x].neighbors.add_edge(self.matrix[y][x-1])

    def node_at(self, x, y):
        return self.matrix[y][x]
