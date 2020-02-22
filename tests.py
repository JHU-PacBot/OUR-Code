import A_Star as AS
from WeightedGraphNode import *
import unittest

class Test_A_Star(unittest.TestCase):
    def test_1(self):
        node1 = WeightedGraphNode(0, 0, 0)
        node2 = WeightedGraphNode(10, 0, 1)
        node3 = WeightedGraphNode(-20, 1, 0)
        node4 = WeightedGraphNode(-20, 1, 1)

        node1.add_edge(node2)
        node1.add_edge(node3)

        node2.add_edge(node4)
        node3.add_edge(node4)

        result_node = AS.a_star(node1, node4)

        self.assertEqual(result_node.graphNode, node4)
        self.assertEqual(result_node.priorPathNode.graphNode, node3)

if __name__ == '__main__':
    unittest.main()
