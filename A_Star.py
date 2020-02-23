import heapq
import MazeGraphMatrix
import constants


def heuristic(start, end):
    # TODO
    # -a little per pellet along the route, + a lot if ghost is in way
    return abs(start.x - end.x) + abs(start.y - end.y)


def a_star(start, goal, graph):
    # maintain a priority queue of paths, going until we reach the goal

    # the number is the output of the heuristic, which gives us a good idea of where to start looking

    pq = [(0, start)]
    # start node gets 0 cost

    current_node = start

    # add the other nodes in the graph
    for row in graph.matrix:
        for node in row:
            if node is not None:
                # there is a node at this spot in the graph

                # add the node to the pq with an initial weight equal to the heuristic (plus a lot)
                node.heuristicWeight = h = heuristic(start, node)
                pq.append((h + 100000, node))

    # keep running until either reach the goal or run out of paths to pop
    while current_node != goal and len(pq) > 0:
        # decompose the tuple to get the node itself
        current_node = heapq.heappop(pq)[0]
        current_node.visited = True

        for neighbor in current_node.graphNode.neighbors:
            # possibly update the paths to all adjacent nodes

            # edge value is constant
            if current_node.graphWeight + constants.EDGE_WEIGHT < neighbor.graphWeight:
                # found a better path, so add it

                neighbor.previousNode = current_node

                neighbor.graphWeight = current_node.weight + constants.EDGE_WEIGHT
                # the value with the heuristic added
                h = neighbor.graphWeight + heuristic(start, neighbor)

                if neighbor.visited:
                    # need to add neighbor back into queue (according to Wikipedia, this is
                    # necessary for "admissible but not consistent" heuristic functions, as
                    # I believe ours will be)
                    neighbor.visited = False
                    heapq.heappush(pq, (h, neighbor))


    # at this point, current_node should contain the goal graph node and the shortest path
    return goal
