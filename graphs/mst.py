import math
import re
import unittest
from math import inf
import heapq

def prim(graph):

    source = list(graph.keys())[0] # Start vertex.
    visited = set([source]) 
    tree = {} # Minimum spanning tree.
    
    # Edges priority queue, sorted increasing by cost.
    edges = [(cost, source, to) for (to, cost) in graph[source]]
    heapq.heapify(edges)

    while edges:
        # Pop edge with lowest cost.
        cost, frm, neighbour = heapq.heappop(edges)
        if neighbour not in visited:
            visited.add(neighbour)
            
            # Update tree
            if frm not in tree:
                tree[frm] = []
            if neighbour not in tree:
                tree[neighbour] = []
            
            tree[frm].append(neighbour)
            tree[neighbour].append(frm)

            # Add neighbour edges to unvisited nodes. 
            for to_next, cost in graph[neighbour]:
                if to_next not in visited:
                    heapq.heappush(edges, (cost, neighbour, to_next))
                    
    return tree

case = {
        "A": [("B", 1), ("D", 3)],
        "B": [("A", 1), ("E", 6), ("C", 3), ("D", 2), ("F", 5)],
        "C": [("B", 3), ("F", 4), ("E", 4)],
        "D": [("A", 3), ("E", 3), ("B", 2)],
        "E": [("D", 3), ("B", 6), ("F", 2), ("C", 4)],
        "F": [("E", 2), ("C", 4), ("B", 5)]
    }  
print("dafq")
print(prim(case))


class Tests(unittest.TestCase):

    case = {
        "A": [("B", 1), ("D", 3)],
        "B": [("A", 1), ("E", 6), ("C", 3), ("D", 2), ("F", 5)],
        "C": [("B", 3), ("F", 4), ("E", 4)],
        "D": [("A", 3), ("E", 3), ("B", 2)],
        "E": [("D", 3), ("B", 6), ("F", 2), ("C", 4)],
        "F": [("E", 2), ("C", 4), ("B", 5)]
    }   


    def test_prim(self):
        pass

