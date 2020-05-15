def tw_partition(lst, key,  l, h):
    m = l
    while m < h:
        if lst[m] < key:
            lst[m], lst[l] = lst[l], lst[m]
            m += 1
            l += 1

        elif lst[m] == key:
            m += 1

        else:
            lst[m], lst[h-1] = lst[h-1], lst[m]
            h -= 1

    #print(lst)
    return l, h


def tw_qsort(lst, l, h):
    if h - l > 1:
        lp, hp = tw_partition(lst, lst[l], l, h)
        tw_qsort(lst, l, lp)
        tw_qsort(lst, hp, h)


if __name__ == '__main__':
    n = 100
    import random
    import time
    lst = [random.choice("abcde") for _ in range(n)]
    start = time.time()
    tw_qsort(lst, 0, n)
    if len(lst) < 200:
        print(lst)
    print(time.time() - start)