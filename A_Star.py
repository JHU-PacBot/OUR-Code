import heapq
import PathNode


def heuristic(start, end):
    # TODO
    # -a little per pellet along the route, + a lot if ghost is in way
    return abs(start.x - end.x) + abs(start.y - end.y)


def a_star(start, goal):
    # maintain a priority queue of paths, going until we reach the goal

    pq = [(0, PathNode.PathNode(start))]
    # start node gets 0 cost

    current_path_node = pq[0]

    # keep running until either reach the goal or run out of paths to pop
    while current_path_node.graphNode != goal and len(pq) > 0:

        # decompose the tuple to get the path node itself
        (_, current_path_node) = heapq.heappop(pq)

        for neighbor in current_path_node.graphNode.neighbors:
            # add the adjacent nodes in the graph to the heap as new paths
            heapq.heappush(pq, (
                current_path_node.WeightedGraphNode.weight() + neighbor.WeightedGraphNode.weight() +
                heuristic(current_path_node, neighbor),
                PathNode.PathNode(neighbor, current_path_node)))

    # at this point, current_path_node should contain the goal graph node and the shortest path
    return current_path_node
