class PathNode:

    def __init__(self, graph_node, prior_path_node=None):
        # self.cost = prior_path_node.cost + graph_node.weight
        self.priorPathNode = prior_path_node
        self.graphNode = graph_node

    """def cost(self):
        if self.priorPathNode is None:
            return 0
        # return the cost of the path leading up to this element
        return self.graphNode.weight + self.priorPathNode.cost()"""
