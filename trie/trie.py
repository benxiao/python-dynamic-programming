class TrieNode:
    __slots__ = ['_count', '_links']

    def __init__(self):
        self._count = 1
        self._links = {}

    def link(self, ch):
        nxt = self._links.get(ch)
        if nxt:
            nxt.incr()
            return nxt

        nxt = TrieNode()
        self._links[ch] = nxt
        return nxt

    def path(self, ch):
        nxt = self._links[ch]
        return nxt

    def count(self):
        return self._count

    def incr(self):
        self._count += 1


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.n = 0

    def add(self, value):
        cur = self.root
        for c in value:
            cur = cur.link(c)
        self.n += 1

    def __len__(self):
        return self.n

    def count(self, value):
        cur = self.root
        for c in value:
            cur = cur.path(c)
        return cur.count()



if __name__ == '__main__':
    trie = Trie()
    trie.add("abc")
    trie.add("abd")
    print(trie.count("a"))
    print(trie.count("ab"))
    print(trie.count("abc"))

