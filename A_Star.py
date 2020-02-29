import heapq
import MazeGraphMatrix
import WeightedGraphNode
import WeightedUniEdge
import constants


def heuristic(start, end):
    if not isinstance(start, WeightedGraphNode.WeightedGraphNode):
        return False
    # TODO
    # -a little per pellet along the route, + a lot if ghost is in way
    return abs(start.x - end.x) + abs(start.y - end.y)


def a_star(start, goal, graph):
    # maintain a priority queue of paths, going until we reach the goal

    # the number is the output of the heuristic, which gives us a good idea of where to start looking

    if not isinstance(graph, MazeGraphMatrix.MazeGraphMatrix) or not isinstance(start,
                                                                                WeightedGraphNode.WeightedGraphNode):
        # problem
        return False

    pq = [(0, start)]
    # start node gets 0 cost

    print type(goal)
    current_node = start

    # add the other nodes in the graph
    for row in graph.matrix:
        for node in row:
            if isinstance(node, WeightedGraphNode.WeightedGraphNode):
                # there is a node at this spot in the graph
                # print "from matrix: ", node.__class__

                # add the node to the pq with an initial weight equal to the heuristic (plus a lot)
                pq.append((heuristic(start, node) + 100000, node))

    # keep running until either reach the goal or run out of paths to pop
    while current_node != goal and len(pq) > 0:
        # decompose the tuple to get the node itself
        current_node = heapq.heappop(pq)[1]
        current_node.visited = True

        for neighborEdge in current_node.neighborEdges:
            # possibly update the paths to all adjacent nodes

            # edge value is constant
            if current_node.graphWeight + constants.EDGE_WEIGHT + neighborEdge.weight < neighborEdge.endNode.graphWeight:
                # found a better path, so add it

                neighborEdge.endNode.previousNode = current_node

                neighborEdge.endNode.graphWeight = current_node.graphWeight + constants.EDGE_WEIGHT
                # the value with the heuristic added
                h = neighborEdge.endNode.graphWeight + heuristic(start, neighborEdge.endNode)

                if neighborEdge.endNode.visited:
                    # need to add neighbor back into queue (according to Wikipedia, this is
                    # necessary for "admissible but not consistent" heuristic functions, as
                    # I believe ours will be)
                    neighborEdge.endNode.visited = False
                    heapq.heappush(pq, (h, neighborEdge.endNode))

    # at this point, current_node should contain the goal graph node and the shortest path
    return goal
