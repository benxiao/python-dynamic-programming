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
    print(merge([1,3,5, 7], [2, 4, 6], [0,8, 9]))