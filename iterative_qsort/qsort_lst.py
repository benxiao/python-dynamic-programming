def array_qsort(lst, low, high):
    def partition(low, high):
        nonlocal lst
        # use the last value as the pivot
        # use j-1 as the last reachable index adheres to python convention
        last_idx = high - 1
        pivot = lst[last_idx]
        i = low - 1
        for k in range(low, last_idx):
            val_idx_k = lst[k]
            if val_idx_k < pivot:
                i += 1
                lst[i], lst[k] = val_idx_k, lst[i]
        i += 1
        lst[i], lst[last_idx] = pivot, lst[i]
        return i

    # initial call
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        p = partition(low, high)
        if p > low+1:
            stack.append((low, p))

        if high > p+2:
            stack.append((p+1, high))


if __name__ == '__main__':
    import random
    import time
    start = time.time()
    lst = [random.randint(0, 10000000) for _ in range(1000000)]
    array_qsort(lst, 0, len(lst))
    print(f'elapsed: {time.time() - start:.2f}s')



#
# if __name__ == '__main__':
#
#     n = Node(3, nxt=Node(1, nxt=Node(5, nxt=Node(4))))
#
#
#     import random
#     import time
#     l = [random.randint(1, 100000) for _ in range(1000000)]
#     start = time.time()
#     sl = to_sll(l)
#     f, l = qsort(sl)
#     print(f)
#     print(time.time() - start)


