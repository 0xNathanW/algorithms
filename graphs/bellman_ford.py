from math import inf

def bf(graph, src):

    dist = {v: inf for v in graph}
    dist[src] = 0

    for _ in range(len(graph)-1):
        for v in graph:
            for e, c in graph[v]:
                dist[e] = min(dist[e], dist[v] + c)
                
    for v in graph:
        for e, c in graph[v]:
            new = dist[v] + c
            if new < dist[e]:
                print("negative cycle found")
    
    return dist

non_neg_graph = {   # Node, distance
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: []
    }

neg_graph = {   # Node, distance
        0: [(1, 3)],
        1: [(2, -5)],
        2: [(3, 4)],
        3: [(0, -6)],
        4: [(0, 5)]
    }

print(bf(neg_graph, 0) )