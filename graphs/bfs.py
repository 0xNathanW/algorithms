from ast import Pass
from collections import deque
from hashlib import new
import unittest

## Assuming graphs are repersented as adjecency lists (dict).

# graph, src - source.
def bfs(graph, src):
    # keep track of already visited vertices.
    seen = set(src)
    q = deque([src])

    while q:
        v = q.pop()
        for e in graph[v]:
            if e not in seen:
                seen.add(e)
                q.appendleft(e)
                print(e)

# Finds the shortest path from source to target.
def shortest_path(graph, src, target):
    
    seen = set(src)
    dist = {src: 0}
    q = deque([src])

    while q:
        v = q.pop()
        for e in graph[v]:
            if e not in seen:
                seen.add(e)
                q.appendleft(e)
                dist[e] = dist[v] + 1
                if e == target:
                    break
    return dist[target]

def shortest_path2(graph, source, target):
    
    queue = [[source]]
    visited = set()

    if source == target: 
        return queue[0]

    while queue:
        
        path = queue.pop(0)
        vertex = path[-1]

        if vertex not in visited:
            for neighbour in graph[vertex]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == target:
                    return new_path
            
            visited.add(vertex)
    
    raise Exception("Connecting path does not exist")

# Graph must be undirected.
def connected_components(graph):
    n = 0
    seen = set()
    for i in graph:
        if i not in seen:
            n += 1 
            q = deque([i])
            while q:
                v = q.pop()
                for e in graph[v]:
                    if e not in seen:
                        seen.add(e)
                        q.appendleft(e)
    return n    

class Tests(unittest.TestCase):


    def test_connected_components(self): 
        s = {
            1: [3, 5],
            3: [1, 5], 
            5: [1, 3, 7, 9],
            7: [5],
            9: [5],
            2: [4], 
            4: [2],
            6: [8, 10],
            8: [6, 10],
            10: [6, 8],
        }
        self.assertEqual(connected_components(s), 3)

    def test_shortest_path(self):
        t = {
            "H": ["D", "E", "F", "G"],
            "E": ["B", "H"],
            "D": ["B", "H"],
            "F": ["H", "C"],
            "G": ["C", "H"],
            "B": ["D", "A", "E"], 
            "C": ["A", "F", "G"], 
            "A": ["B", "C"]
        }
        self.assertEqual(shortest_path(t, "H", "A"), 3)
        self.assertEqual(shortest_path(t, "F", "A"), 2)
        self.assertEqual(shortest_path(t, "B", "F"), 3)
        self.assertEqual(shortest_path(t, "B", "D"), 1)

t = {
            "H": ["D", "E", "F", "G"],
            "E": ["B", "H"],
            "D": ["B", "H"],
            "F": ["H", "C"],
            "G": ["C", "H"],
            "B": ["D", "A", "E"], 
            "C": ["A", "F", "G"], 
            "A": ["B", "C"]
        }        

print(shortest_path2(t, "H", "A"))

# unittest.main()


