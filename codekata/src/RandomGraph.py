from Graph import Vertex
from Graph import Edge
from Graph import Graph
import unittest
import random
"""
define a class named RandomGraph that inherits from Graph and provides a method 
named add_random_edges that takes a probability p as a parameter and, 
starting with an edgeless graph, adds edges at random so that 
the probability is p that there is an edge between any two nodes.
"""

class RandomGraph(Graph):
    
    def add_random_edges(self, p):
        if p < 0 or p > 1:
            raise ValueError("p is a probability which range is [0, 1]")
        verticies = self.vertices()
        unvisitedVertices = set(verticies)
        for vertexA in vertices:
            for vertexB in self[vertexA]:
                if vertexB == vertexA:
                    continue
                if vertexB not in unvisitedVertices:
                    continue
                if random.random() <= p:
                    self.add_edge(Edge(vertexA, vertexB))




class RandomGraphTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_random_edges(self):
        v = Vertex('v')
        w = Vertex('w')
        e = Edge(v, w)
        g = RandomGraph([v, w], [e])

if __name__ == '__main__':
    unittest.main()