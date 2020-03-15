import graphviz as gv


class HeightBasedUnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.h = [1] * n

    def __str__(self):
        return f"UF\n{self.id=}\n{self.h=}\n"

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.h[i] > self.h[j]:
            self.id[j] = i
            self.h[i] = max(self.h[i], self.h[j]+1)
        else:
            self.id[i] = j
            self.h[j] = max(self.h[j], self.h[i]+1)

    def viz(self):
        dg = gv.Digraph()
        for i, j in enumerate(self.id):
            dg.edge(str(i), str(j))
        dg.render(view=True)


class WeightedUnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.sz = [1] * n
        self.count = n

    def __len__(self):
        return len(self.id)

    def __str__(self):
        return f"UF\n{self.id=}\n{self.sz=}\n"

    def connected(self, p, q) -> bool:
        return self.find(p) == self.find(q)

    def find(self, p):
        ids_on_path = []
        while p != self.id[p]:
            ids_on_path.append(p)
            p = self.id[p]

        while ids_on_path:
            self.id[ids_on_path.pop()] = p
        return p

    def viz(self):
        dg = gv.Digraph()
        for i, j in enumerate(self.id):
            dg.edge(str(i), str(j))
        dg.render(view=True)

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz[i] >= self.sz[j]:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        else:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        self.count -= 1


if __name__ == '__main__':
    uf = HeightBasedUnionFind(10)
    print(uf)
    uf.union(0, 1)
    print(uf)
    uf.union(2, 3)
    print(uf)
    uf.union(4, 5)
    print(uf)
    uf.union(6, 7)
    print(uf)
    uf.union(0, 2)
    print(uf)
    uf.union(4, 6)
    print(uf)
    uf.union(0, 4)
    # print(uf)
    # uf.connected(5, 0)
    # print(uf)
    # #uf.graphviz()
    uf.union(7, 8)
    # print(uf)
    #uf.union(0, 8)

    uf.union(3, 5)
    uf.viz()
