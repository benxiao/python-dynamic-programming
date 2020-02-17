from functools import total_ordering


@total_ordering
class Node:

    __slots__ = ['_val','_nxt']

    def __init__(self, val, nxt=None):
        self._val = val
        self._nxt = nxt

    def val(self):
        return self._val

    def next(self):
        return self._nxt

    def set_next(self, n):
        self._nxt = n

    def __lt__(self, other):
        assert isinstance(other, Node)
        return self._val < other._val

    def __eq__(self, other):
        assert isinstance(other, Node)
        return self._val == other._val

    def count(self):
        return sum(1 for _ in self)

    def __iter__(self):
        cur = self
        while cur:
            yield cur
            cur = cur.next()

    def __str__(self):
       return "->".join(str(x._val) for x in self)

    __repr__ = __str__


def to_sll(x):
    sentinel = Node(None)
    cur = sentinel
    for e in x:
        cur.set_next(Node(e))
        cur = cur.next()
    return sentinel.next()


def partition(l):
    val = l.val()
    left_sentinel = Node(None)
    left_tail = left_sentinel
    right_sentinel = Node(None)
    right_tail = right_sentinel
    if not l.next():
        return None, val, None

    for node in l.next():
        if node.val() < val:
            left_tail.set_next(node)
            left_tail = left_tail.next()
        else:
            right_tail.set_next(node)
            right_tail = right_tail.next()

    right_tail.set_next(None)
    left_tail.set_next(None)
    return left_sentinel.next(), val, right_sentinel.next()


def qsort(l):
    if l is None:
        return None, None
    left, val, right = partition(l)
    pivot = Node(val)
    lfp, llp = qsort(left)
    rfp, rlp = qsort(right)
    if lfp is None:
        lfp = pivot
    else:
        llp.set_next(pivot)
    if rfp is None:
        rlp = pivot
    else:
        pivot.set_next(rfp)
    return lfp, rlp