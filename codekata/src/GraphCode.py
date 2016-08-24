""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
import unittest

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError('Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
    def get_edge(self, v, w):
        try:
            return self[v][w]
        except Exception as e:
            return None

    def remove_edge(self, e):
        v = e[0]
        w = e[1]
        del self[v][w]
        del self[w][v]

    def vertices(self):
        return list(self.keys())

    def edges(self):
        """returns a list of Edges in this graph"""
        vertices = self.vertices()
        edges = set()
        for v in vertices:
            for edge in self[v].values():
                if edge not in edges:
                    edges.add(edge)
        return list(edges)

    def out_vertices(self, v):
        """takes a vertix and returns a list of the adjacent vertices"""
        return list(self[v].keys())

    def out_edges(self, v):
        """ takes a Vertex and returns a list of edges connected to the given Vertex. """
        return list(self[v].values())

    def add_all_edges(self):
        """ makes a complete graph by adding edges between all pairs of vertices. """
        vertices = self.vertices()
        if len(vertices) < 2: 
            return
        for vertexA in vertices:
            for vertexB in vertices:
                if vertexA == vertexB:
                    continue
                self.add_edge(Edge(vertexA, vertexB))

    def add_regular_edges(self, degree):
        """starts with an edgeless graph and adds edges so that every vertex has the same degree."""

        pass

class GraphCodeTest(unittest.TestCase):
    def setUp(self):
        self.data = data = type('test', (object,), {})()
        v = data.v = Vertex('v')
        w = data.w = Vertex('w')
        e = data.e = Edge(v, w)
        data.g = Graph([v,w], [e])

    def testEdges(self):
        data = self.data
        self.assertEqual([data.e], data.g.edges())

    def testOutVertices(self):
        data = self.data
        self.assertEqual(data.g.out_vertices(data.v), [data.w])

    def testOutEdges(self):
        data = self.data
        self.assertEqual(data.g.out_edges(data.v), [data.e])


def main(script, *args):
    v = Vertex('v')
    print(v)
    w = Vertex('w')
    print(w)
    e = Edge(v, w)
    print(e)
    g = Graph([v,w], [e])
    print(g)
    e = g.get_edge(v, w)
    print(e)
    print(g.edges())
    g.remove_edge(e)
    print(g)
    print(g.vertices())
    


if __name__ == '__main__':
    import sys
    unittest.main()
    main(*sys.argv)
