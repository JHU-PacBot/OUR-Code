import constants

class WeightedUniEdge:
    def __init__(self, end, weight):
        # add the constant "we're going somewhere, and that costs" weight to the edge
        self.weight = weight + constants.EDGE_WEIGHT
        self.endNode = end


