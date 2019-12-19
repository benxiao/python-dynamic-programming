inf = float("infinity")

V = 4
edges = {
    (1, 0): 4,
    (1, 2): 3,
    (2, 3): 2,
    (3, 1): -1,
    (0, 2): -2
}

"""
Floyd–Warshall algorithm
"""

def floyd_warshall(edges, V):

    cache = [[inf] * V for _ in range(V)]
    paths = [[[] for _ in range(V)] for _ in range(V)]

    for i in range(V):
        cache[i][i] = 0

    for ef, et in edges:
        cache[ef][et] = edges[(ef, et)]

    for row in cache:
        print(row)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if cache[i][j] > cache[i][k] + cache[k][j]:
                    cache[i][j] = cache[i][k] + cache[k][j]
                    paths[i][j] = paths[i][k] + [k] + paths[k][j]

    return cache, paths

##################################################################
"""
Bellman-Ford
"""
def bellman_ford(edges, V, src):
    cache = [inf] * V
    cache[src] = 0
    prev = [None] * V

    for i in range(V-1):
        for e, w in edges.items():
            ef, et = e
            relaxed_weight = cache[ef] + w
            if relaxed_weight  < cache[et]:
                cache[et] = relaxed_weight
                prev[et] = ef

    print(cache)
    print(prev)
    # check for negative cycles
    for e, w in edges.items():
        ef, et = e
        if cache[ef] + w < cache[et]:
            raise ValueError("negative cycle detected")

    return cache, prev






if __name__ == '__main__':
    bellman_ford(edges, 4,  0)