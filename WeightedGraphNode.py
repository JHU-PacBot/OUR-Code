class WeightedGraphNode:
    def __init__(self, weight, x, y):
        self.weight = weight
        self.neighbors = []
        self.x = x
        self.y = y

    def weight(self):
        return self.weight

    def add_edge(self, neighbor):
        self.neighbors.append(neighbor)
