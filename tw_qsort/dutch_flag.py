import random
random.seed(42)


def dutch(lst, key,  l, h):
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

    print(lst)
    return l, h

n = 100
lst = [random.choice([0, 1, 2]) for _ in range(n)]
print(lst)
print(dutch(lst, 1, 0, n))
