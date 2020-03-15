import heapq
import random
import graphviz as gv
from typing import *

from functools import total_ordering
from uf import WeightedUnionFind

random.seed(42)


@total_ordering
class Edge:
    __slots__ = ['_a', '_b', '_w']

    def __init__(self, a, b, w):
        self._a = a
        self._b = b
        self._w = w

    def __lt__(self, other):
        if not isinstance(other, Edge):
            raise TypeError()
        return (self._w, self._a, self._b) < (other._w, other._a, other._b)

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return (self._w, self._a, self._b) == (other._w, other._a, other._b)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def w(self):
        return self._w

    def __str__(self):
        return f"Edge<{self._a},{self._b}|{self._w:.2f}>"

    __repr__ = __str__


class DWG:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]

    def __len__(self):
        return len(self.adj)

    def add(self, i, j, w):
        e = Edge(i, j, w)
        self.adj[i].append(e)

    def __str__(self):
        return str(self.adj)

    def all_edges(self):
        for g in self.adj:
            for e in g:
                yield e

class WG:
    def __init__(self, n):
        self.adj: List[List[Edge]] = [[] for _ in range(n)]

    def __len__(self):
        return len(self.adj)

    def connected(self, i, j):
        for e in self.adj[i]:
            if e.b == j:
                return True

    def add(self, i, j, w):
        edge = Edge(i, j, w)
        reversed_edge = Edge(j, i, w)
        self.adj[i].append(edge)
        self.adj[j].append(reversed_edge)

    def __str__(self):
        return str(self.adj)

    def all_edges(self):
        for g in self.adj:
            for e in g:
                yield e

    def random(self, n=2):
        n = len(self.adj)
        for i in range(n):
            for _ in range(2):
                j = random.randint(0, n-1)
                if not self.connected(i, j) and i != j:
                    self.add(i, j, random.random())

    def viz(self):
        view = gv.Graph()
        for g in self.adj:
            for e in g:
                if e.a <= e.b:
                    view.edge(str(e.a), str(e.b), label=f"{e.w:.2f}")
        view.render(view=True)


def kruskal_algo(graph):
    uf = WeightedUnionFind(len(graph))
    edges = list(graph.all_edges())
    edges.sort(reverse=True)
    edges_in_mst = []
    while uf.count > 1:
        if not edges:
            raise ValueError("no mst here!")
        e = edges.pop()
        if not uf.connected(e.a, e.b):
            uf.union(e.a, e.b)
            edges_in_mst.append(e)
    return edges_in_mst


def prim_algo(graph):
    min_heap = []
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    i = 1
    for e in graph.adj[0]:
        heapq.heappush(min_heap, e)

    edges_in_mst = []
    while i < n:
        while 1:
            edge = heapq.heappop(min_heap)
            if not visited[edge.b]:
                visited[edge.b] = True
                edges_in_mst.append(edge)
                i += 1
                break

        new_node = edges_in_mst[-1].b
        for e in graph.adj[new_node]:
            heapq.heappush(min_heap, e)

    return edges_in_mst


def draw_result(graph):
    edges_in_mst = prim_algo(graph)
    visual_rep = gv.Graph()
    for g in graph.adj:
        for e in g:
            if e.a < e.b and e not in edges_in_mst:
                visual_rep.edge(str(e.a), str(e.b), label=f"{e.w:.2f}")
    for e in edges_in_mst:
        visual_rep.edge(str(e.a), str(e.b), color='blue', label=f"{e.w:.2f}")
    visual_rep.view()


if __name__ == '__main__':
    g = WG(10)
    g.random(2)
   # print(g.adj)
    #g.viz()
    print(kruskal_algo(g))
    print(prim_algo(g))
    draw_result(g)
    #print(kruskal_algo(dg))


