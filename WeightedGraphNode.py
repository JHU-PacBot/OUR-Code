class WeightedGraphNode:
    def __init__(self, weight, x, y):
        self.weight = weight
        self.neighbors = []
        self.x = x
        self.y = y

    def weight(self):
        return self.weight

    def add_edge(self, neighbor):
        # add bidirectionally
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other
