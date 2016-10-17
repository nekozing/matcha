from Graph import Vertex
from Graph import Edge
from Graph import Graph
import unittest
import random
import string
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
        visitedVerticies = set()
        for vertexA in verticies:
            visitedVerticies.add(vertexA)
            for vertexB in verticies:
                if vertexB == vertexA:
                    continue
                if vertexB in visitedVerticies:
                    continue
                if random.random() <= p:
                    edge = Edge(vertexA, vertexB)
                    self.add_edge(edge)


class RandomGraphTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_random_edges(self):
        v = Vertex('v')
        w = Vertex('w')
        e = Edge(v, w)
        g = RandomGraph([v, w], [e])

    def test_erdos(self):
        n = 50
        p = 0.15
        labels = string.ascii_lowercase + string.ascii_uppercase
        
        connected_count = 0.0
        experiment_count = 100
        for i in range(experiment_count):
            vs = [Vertex(c) for c in labels[:n]]
            g = RandomGraph(vs)
            g.add_random_edges(p)
            if g.is_connected(): connected_count += 1
        print "random graph of {:d} vertices and p {:.2f} has {:.2f} of being connected".format(n, p, connected_count/experiment_count) 

if __name__ == '__main__':
    unittest.main()