from math import inf

def bf(graph, src):

    dist = {v: inf for v in graph}
    dist[src] = 0

    for _ in range(len(graph)-1):
        for v in graph:
            for e, c in graph[v]:
                dist[e] = min(dist[e], dist[v] + c)
                
