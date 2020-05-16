def tw_tp_partition(lst, lp, hp, l, h):
    while lst[l] < lp:
        l += 1

    while lst[h-1] > hp:
        h -= 1
    m = l
    while m < h:
        if lst[m] <= lp:
            lst[m], lst[l] = lst[l], lst[m]
            m += 1
            l += 1

        elif lp < lst[m] < hp:
            m += 1

        else:
            lst[m], lst[h-1] = lst[h-1], lst[m]
            h -= 1
    return l, h


def tw_tp_qsort(lst, l, h):
    if h - l > 1:
        lp, hp = lst[l], lst[h-1]
        if lp > hp:
            lp, hp = hp, lp
        nl, nh = tw_tp_partition(lst, lp, hp, l, h)
        if nl == h:
            return
        tw_tp_qsort(lst, l, nl)
        tw_tp_qsort(lst, nl, nh)
        tw_tp_qsort(lst, nh, h)
        

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

    return l, h


def tw_qsort(lst, l, h):
    if h - l > 1:
        lp, hp = tw_partition(lst, lst[l], l, h)
        tw_qsort(lst, l, lp)
        tw_qsort(lst, hp, h)


if __name__ == '__main__':
    n = 1000_000
    import random
    import time
    lst = [random.choice(range(0, 30)) for _ in range(n)]
    start = time.time()
    #lst = [4, 3]
    #tw_tp_partition(lst, 1, 3, 0, n)
    tw_tp_qsort(lst, 0, n)
    print(lst)

    # tw_tp_qsort(lst, 0, n)
    # if len(lst) < 200:
    #     print(lst)
    print(time.time() - start)