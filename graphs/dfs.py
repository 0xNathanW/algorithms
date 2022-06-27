from msilib.schema import Component
import unittest

def dfs(graph, vertex, visited=set()):
	
    if vertex not in visited:  # Skip if vertex already seen.
        visited.add(vertex)    # Add to visited.
	
        for neighbour in graph[vertex]:       # Iterate neighbours.
	        dfs(graph, neighbour, visited)    # DFS on each neighbour.


# Only works on directed acyclic graphs.
# Returns topological ordering.
def topological_sort(graph):

    visited = set()  # Keep track of visited vertices.
    stack = []       # Where topological ordering is stored.
	
    # Nested DFS function.
    def dfs(graph, source, visited, stack):
        visited.add(source)  # Add to visited.
		
        for neighbour in graph[source]:  # Iterate neighbours.
            if neighbour not in visited:
                dfs(graph, neighbour, visited, stack)

        stack.append(source)  # Add in reverse order on call-back.
	
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited, stack)

    return stack[::-1] # Return the topological ordering.


# Computes strongly connected component of the graph.
def kosaraju(graph):
    
    visited = set()
    stack = []  # Highest finishing time at top of stack.

    def dfs(graph, source):
        visited.add(source)
        
        for neighbour in graph[source]:
            if neighbour not in visited:
                dfs(graph, neighbour)
        
        stack.append(source)
    
    # 1st DFS pass.
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex)

    # Create a reversed graph.
    reversed = {vertex: [] for vertex in graph.keys()}
    for vertex, neighbours in graph.items():
        for neighbour in neighbours:
                reversed[neighbour].append(vertex)
    
    visited = set()    # Reset visited.
    components = []    # Stores strongly connected components.

    def dfs2(graph, source, component):
        visited.add(source)
        component.append(source)
        for neighbour in graph[source]:
            if neighbour not in visited:
                dfs2(graph, neighbour, component)

    # 2nd DFS pass.
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            component = []
            dfs2(reversed, vertex, component)
            components.append(component)
        
    return components


class Tests(unittest.TestCase):

    def test_topological_sort(self):
        case = {
                6: [1, 5], 
                5: [3, 4],
                1: [2, 5],
                0: [1, 2],
                2: [3],
                3: [], 
                4: [],
            }
        self.assertEqual(topological_sort(case), [0, 6, 1, 5, 4, 2, 3])
    
    def test_kosaraju(self):
        case = {
            1: [5],
            2: [3],
            3: [4],
            4: [2, 5],
            5: [6],
            6: [9, 1],
            7: [8],
            8: [9],
            9: [7],
        }
        self.assertCountEqual(kosaraju(case), [[2, 4, 3], [1, 6, 5], [9, 8, 7]])

unittest.main()
		