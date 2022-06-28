from turtle import distance
import unittest 
from math import inf
import heapq

def lazy_dijkstras(graph, source):

    # Tracks shortest distance to each vertex. 
    distances = {vertex: inf for vertex in graph}
    distances[source] = 0                           
    visited = set()

    # Min heap, key is distance.
    priorityQ = [(0, source)]
    while priorityQ:

        min_dist, vertex = heapq.heappop(priorityQ) # Pop most promising node.
        visited.add(vertex)
        if distances[vertex] < min_dist:
            continue

        for neighbour, cost in graph[vertex]: # Iterate neighbours.
            if neighbour in visited:
                continue
            
            # Compute new distance.
            new_distance = distances[vertex] + cost

            # Compare with current shortest.
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heapq.heappush(priorityQ, (new_distance, neighbour))

    return distances





    

    # while queue:

    #     vertex = heapq.heappop(queue)
    #     for neighbour in graph[vertex]:

    #         if neighbour not in distances:
    #             best_distance = distances[vertex]
    # pass

graph = {   # Node, distance
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}   # https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/

print(lazy_dijkstras(graph, 0))