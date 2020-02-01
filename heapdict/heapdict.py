
heap = [None]

MINIMUM_VALUE = - (2 ** 64)


def left(x):
    return x << 1


def right(x):
    return x << 1 + 1


def parent(x):
    return x >> 1


def heapsink(_heap, _dict, idx, debug=False):
    """
    sink the item at idx
    """
    pos = idx

    while left(pos) < len(_heap):
        left_idx = left(pos)
        smaller = left_idx
        right_idx = left_idx + 1
        if right_idx < len(_heap):
            if _heap[left_idx][0] > _heap[right_idx][0]:
                smaller = right_idx

        if _heap[smaller][0] >= _heap[pos][0]:
            break

        _heap[smaller], _heap[pos] = _heap[pos], _heap[smaller]
        _dict[_heap[smaller][1]], _dict[_heap[pos][1]] = _dict[_heap[pos][1]], _dict[_heap[smaller][1]]
        pos = smaller

    if debug:
        check_invariants(_heap, _dict)


def heappop(_heap, _dict, debug=False):
    """
    remove the first element
    """
    if len(_heap) > 1:
        first = _heap[1]
        first_key, first_value = first
        del _dict[first_value]
        if len(_dict) == 0:
            _heap.pop()
        else:
            _heap[1] = _heap.pop()
            priority, key = _heap[1]
            _dict[key] = 1
            heapsink(_heap, _dict, 1)
        if debug:
            check_invariants(_heap, _dict)
        return first

    else:
        raise ValueError("heap is empty")


def heapremove(_heap, _dict, key, debug=False):
    """
    remove a key in the heap
    """
    # will catch key error
    idx = _dict[key]
    _heap[idx] = (MINIMUM_VALUE, key)
    heapfloat(_heap, _dict, idx)
    heappop(_heap, _dict)
    if debug:
        check_invariants(_heap, _dict)


def heapupdate(_heap, _dict, key, priority, debug=False):
    """
    update a key in the heap with new priority
    """
    idx = _dict[key]
    old_priority, key = _heap[idx]
    _heap[idx] = (priority, key)
    if priority > old_priority:
        heapsink(_heap, _dict, idx)
    else:
        heapfloat(_heap, _dict, idx)
    if debug:
        check_invariants(_heap, _dict)


def heapfloat(_heap, _dict, idx, debug=False):
    """
    float the item at position idx
    """

    pos = idx
    while pos > 1 and _heap[pos][0] < _heap[parent(pos)][0]:
        parent_pos = parent(pos)
        _heap[pos], _heap[parent_pos] = _heap[parent_pos], _heap[pos]
        child_key = _heap[pos][1]
        parent_key = _heap[parent_pos][1]
        _dict[child_key], _dict[parent_key] = _dict[parent_key], _dict[child_key]
        pos = parent(idx)
    if debug:
        check_invariants(_heap, _dict)


def heappush(_heap, _dict, key, priority, debug=False):
    """
    push a new item on the _heap
    """
    if _dict.get(key):
        raise ValueError()

    _heap.append((priority, key))
    idx = len(_heap) - 1
    _dict[key] = idx
    heapfloat(_heap, _dict, idx)
    if debug:
        check_invariants(_heap, _dict)


def check_invariants(_heap, _dict):
    """
    check to make sure key invariants are not broken
    """
    for i in range(1, len(_heap)):
        p, _ = _heap[i]
        if left(i) < len(_heap):
            lp, _ = _heap[left(i)]
            if p > lp:
                raise ValueError(f"left child smaller ({left(i)})")

        if right(i) < len(_heap):
            rp, _ = _heap[right(i)]
            if p > rp:
                raise ValueError(f"right child smaller ({right(i)})")

    for k in _dict:
        if k != _heap[_dict[k]][1]:
            raise ValueError("dict is not updated properly")


class HeapDict:
    def __init__(self):
        self._lst = [None]
        self._dict = {}

    def __str__(self):
        return str(self._lst) + "\n" + str(self._dict)

    def push(self, key, priority, debug=False):
        heappush(self._lst, self._dict, key, priority, debug=debug)

    def pop(self, debug=False):
        return heappop(self._lst, self._dict, debug=debug)

    def update(self, key, priority, debug=False):
        heapupdate(self._lst, self._dict,  key, priority, debug=debug)


if __name__ == '__main__':
    hd = HeapDict()
    hd.push("a", 6)
    hd.push("b", 7)
    hd.push("c", 3)
    print(hd)
    hd.pop()
    print(hd)
    hd.pop()
    print(hd)
    hd.pop()
    print(hd)
