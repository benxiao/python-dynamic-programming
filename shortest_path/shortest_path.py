from heapdict import HeapDict

inf = float("infinity")

V = 4
edges = {
    (1, 0): 4,
    (1, 2): 3,
    (2, 3): 2,
    (3, 1): -1,
    (0, 2): -2
}

dijkstra_edges = {
    0: [(1, 2), (2, 5)],
    1: [(0, 2), (2, 2)],
    2: [(0, 5), (1, 2)]

}
print(dijkstra_edges)
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


def bellman_ford(edges, V: int, src):
    cache = [inf] * V
    cache[src] = 0
    prev = [None] * V

    for i in range(V - 1):
        for e, w in edges.items():
            ef, et = e
            relaxed_weight = cache[ef] + w
            if relaxed_weight < cache[et]:
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



# def dijkstra_algo(edges, V, src):
#     # memory allocation
#     cache = [inf] * V
#     visited = [False] * V
#     heapdict = HeapDict()
#
#     # initialization
#     cache[src] = 0
#     visited[src] = True
#     cur = src
#     for i in range(V-1):
#         for (w, k) in edges[cur]:
#             if not visited[k]:
#                 heapdict.push(w, k)
#                 new_edge_weight = w + cache[cur]
#                 if cache[k] > new_edge_weight:
#                     cache[k] = new_edge_weight
#                     heapdict.push(w, k)
#
#         while 1:
#             _, v = heapdict.pop()
#             if visited[v]:
#                 continue
#             visited[v] = True
#             cur = v
#             print(cur)
#             break
#
#     return cache


def dijkstra_algo_simplified(edges, V, src):
    # memory allocation
    cache = [inf] * V
    visited = [False] * V

    # initialization
    cache[src] = 0
    visited[src] = True
    cur = src
    for i in range(V-1):
        for (w, k) in edges[cur]:
            if not visited[k]:
                new_edge_weight = w + cache[cur]
                if cache[k] > new_edge_weight:
                    cache[k] = new_edge_weight

        while 1:
            vs = sorted(filter(lambda x: not visited[x], range(V)),
                        key=lambda x: cache[x])
            cur = vs[0]
            print(cur)
            visited[cur] = True
            break

    return cache


adjacent_matrix = \
    [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]]


dijkstra_edges = {}
for i in range(len(adjacent_matrix)):
    dijkstra_edges[i] = []
    for j, w in enumerate(adjacent_matrix[i]):
        if w > 0:
            dijkstra_edges[i].append((w, j))
print(dijkstra_edges)


if __name__ == '__main__':

    # bellman_ford(edges, 4,  0)
    print(dijkstra_algo_simplified(dijkstra_edges, 9, 0))
    #print(dijkstra_algo(dijkstra_edges, 9, 0))
