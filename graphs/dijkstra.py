from turtle import distance
import unittest 
from math import inf
import heapq

def lazy_dijkstras(graph, source):

    # Tracks shortest distance to each vertex. 
    distances = {vertex: inf for vertex in graph}                          
    visited = set()
    # Tracks previous vertex taken to get to vertex i.
    previous = {vertex: None for vertex in graph}
    distances[source] = 0 

    # Min heap, key is distance.
    priorityQ = [(0, source)]
    while priorityQ:
        print(priorityQ)
        min_dist, vertex = heapq.heappop(priorityQ) # Pop most promising node.
        visited.add(vertex)
        if distances[vertex] < min_dist: # Ignores stale nodes (optimisation).
            continue

        for neighbour, cost in graph[vertex]: # Iterate neighbours.
            if neighbour in visited:
                continue
            
            # Compute new distance.
            new_distance = distances[vertex] + cost

            # Compare with current shortest.
            if new_distance < distances[neighbour]:
                previous[neighbour] = vertex
                distances[neighbour] = new_distance
                heapq.heappush(priorityQ, (new_distance, neighbour))

    return distances, previous

def find_shortest_path(graph, source, target):

    distances, previous = lazy_dijkstras(graph, source)
    path = []
    
    if distances[target] == inf: # Target unreachable.
        return path

    while target is not None: # Stop at source.
        path.append(target)
        target = previous[target]
    
    return path[::-1]

class Tests(unittest.TestCase):

    graph = {   # Node, distance
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: []
    } 

    def test_lazy_dijkstras(self):

        d, p = lazy_dijkstras(self.graph, 0)
        print(d)

unittest.main()