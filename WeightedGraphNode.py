import WeightedUniEdge

class WeightedGraphNode:
    def __init__(self, x, y, weight=0):
        # use weighted edges
        self.visited = False
        self.previousNode = None
        self.graphWeight = weight
        self.neighbors = []
        self.x = x
        self.y = y

    def add_edge(self, neighbor, weight=0):
        # add unidirectionally
        self.neighbors.append(WeightedUniEdge.WeightedUniEdge(neighbor, weight))


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other
