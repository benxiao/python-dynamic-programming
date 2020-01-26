import random
random.seed(40)


def shell_sort(lst):
    l = len(lst)
    h = 1
    one_third = l // 3
    n_comparisons = 0
    n_swaps = 0
    while h < one_third:
        h *= 3
        h += 1
    #     print(f"h: {h}")
    # print(f"h: {h}")
    while h >= 1:
        for i in range(h, l):
            for j in range(i, h-1, -h):
                n_comparisons += 1
                if lst[j] >= lst[j-h]:
                    break
                lst[j], lst[j-h] = lst[j-h], lst[j]
                n_swaps += 1

        h //= 3

    #print(f"shell_sort:{lst}")

    return {
        "n_comparisons": n_comparisons,
        "n_swaps": n_swaps
    }


def isort(lst):
    n_comparisons = 0
    n_swaps = 0
    l = len(lst)
    for i in range(1, l):
        for j in range(i, 0, -1):
            n_comparisons += 1
            if lst[j] >= lst[j-1]:

                break
            lst[j], lst[j-1] = lst[j-1], lst[j]
            n_swaps += 1
    #print(f"insert_sort:{lst}")
    return {
        "n_comparisons": n_comparisons,
        "n_swaps": n_swaps
    }


def r_quick_sort(lst, i, j):
    def partition(lst, i, j):
        n_swaps = 0
        n_comparisons = 0
        k = i-1
        p_idx = j-1
        p_value = lst[p_idx]
        for m in range(i, j-1):
            n_comparisons += 1
            if lst[m] < p_value:
                k += 1
                lst[k], lst[m] = lst[m], lst[k]
                n_swaps += 1
        k += 1
        lst[p_idx], lst[k] = lst[k], lst[p_idx]
        n_swaps += 1

        return k, n_swaps, n_comparisons

    if j - i > 1:
        pivot, s, c = partition(lst, i, j)
        # print(f"called with {i}, {pivot}")
        cl, sl = r_quick_sort(lst, i, pivot)
        cr, sr = r_quick_sort(lst, pivot+1, j)
        return s+cl+cr, c+sl+sr
    return 0, 0


def quick_sort(lst):
    c, s = r_quick_sort(lst, 0, len(lst))
    return {
        "n_comparisons": c,
        "n_swaps": s
    }


if __name__ == '__main__':
    a = [random.randint(0, 10000) for _ in range(10000)]
    b = a.copy()
    c = a.copy()
    print("qsort:", quick_sort(c))
    print("shell_sort:", shell_sort(a))
    print("isort:", isort(b))
    print(a)
    print(b)
    print(c)
