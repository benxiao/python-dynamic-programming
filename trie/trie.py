from typing import *
import random


class TrieNode:
    __slots__ = ['_overlay_count','_count', '_links', '_end']

    def __init__(self):
        self._overlay_count = 1
        self._count = 0
        self._links = {}
        self._end = False

    def is_leave(self):
        return not bool(self._links)

    def get_links(self):
        return self._links.keys()

    def link(self, ch):
        nxt = self._links.get(ch)
        if nxt:
            nxt.incr_overlay()
            return nxt
        nxt = TrieNode()
        self._links[ch] = nxt
        return nxt

    def is_end(self):
        return self._end

    def set_end(self):
        self._end = True

    def path(self, ch):
        nxt = self._links[ch]
        return nxt

    def overlay_count(self):
        return self._overlay_count

    def incr_overlay(self):
        self._overlay_count += 1

    def count(self):
        return self._count

    def incr_count(self):
        self._count += 1


class Trie:
    def __init__(self, lst:List[str]=None):
        self.root = TrieNode()
        self.n = 0
        if lst:
            for s in lst:
                self.add(s)

    def add(self, value):
        cur = self.root
        for c in value:
            cur = cur.link(c)
        cur.set_end()
        cur.incr_count()

    def exist(self, value):
        cur = self.root
        for c in value:
            try:
                cur = cur.path(c)
            except KeyError:
                return False
        return cur.is_end()

    def __len__(self):
        return self.n

    def count(self, value):
        cur = self.root
        for c in value:
            cur = cur.path(c)
        return cur.count()


    def overlay_count(self, value):
        cur = self.root
        for c in value:
            cur = cur.path(c)
        return cur.overlay_count()

    def random(self):
        cur = self.root
        characters = []
        while 1:
            c = random.choice(list(cur.get_links()))
            cur = cur.path(c)
            characters.append(c)
            if (cur.is_end() and random.random() < 0.1) or cur.is_leave():
                return "".join(characters), cur.count()

    def random_elements(self, n=5):
        return [self.random() for _ in range(n)]


if __name__ == '__main__':
    trie = Trie()
    trie.add("abc")
    trie.add("abd")
    print(trie.count("a"))
    print(trie.count("ab"))
    print(trie.count("abc"))
    print(trie.exist("a"))
    print(trie.exist("abc"))
    print(trie.random_walk())
    print(trie.random_elements())

