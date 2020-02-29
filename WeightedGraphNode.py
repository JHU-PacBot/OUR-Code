import WeightedUniEdge

class WeightedGraphNode:
    def __init__(self, x, y, weight=0):
        # use weighted edges
        self.visited = False
        self.previousNode = None
        self.graphWeight = weight
        self.neighborEdges = []
        self.x = x
        self.y = y

    def add_edge(self, neighbor, weight=0):
        # add unidirectionally
        self.neighborEdges.append(WeightedUniEdge.WeightedUniEdge(neighbor, weight))

    def __str__(self):
        return self.x + ", " + self.y

    def __eq__(self, other):
        if isinstance(other, WeightedGraphNode):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __ne__(self, other):
        return not self == other
