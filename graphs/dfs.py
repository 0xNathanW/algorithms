import unittest

def dfs(graph, src, seen=set()):
    print(src)
    seen.add(src)
    for e in graph[src]:
        if e not in seen:
            dfs(graph, e, seen)

dfs({
    1: [2, 3],
    2: [4, 5],
    5: [6],
    4: [],
    3: [6],
    6: [],
}, 1)