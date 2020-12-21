"""
Another efficient solution is to use Min Heap. This Min Heap based solution has same time complexity which is O(nk Log k). But for different sized arrays, this solution works much better.

Following is detailed algorithm.
1. Create an output array of size n*k.
2. Create a min heap of size k and insert 1st element in all the arrays into the heap
3. Repeat following steps n*k times.
     a) Get minimum element from heap (minimum is always at root) and store it in output array.
     b) Replace heap root with next element from the array from which the element is extracted. If the array doesn’t have any more elements, then replace root with infinite. After replacing the root, heapify the tree.

Following is the implementation of the above algorithm.
"""

import heapq
from itertools import repeat


def merge(*arrays):
    total = sum(len(a) for a in arrays)
    arrays = [zip(a, repeat(i)) for i, a in enumerate(arrays) if len(a)]
    n = len(arrays)
    heap = []
    for a in arrays:
        item = next(a)
        heapq.heappush(heap, item)
    result = [None] * total
    i = 0
    while n:
        e, k = heapq.heappop(heap)
        result[i] = e
        i += 1
        try:
            next_item = next(arrays[k])
            heapq.heappush(heap, next_item)
        except StopIteration:
            n -= 1

    return result


if __name__ == '__main__':
    print(merge([1, 3, 5, 7], [2, 4, 6], [0, 8, 9]))
