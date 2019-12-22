a = [1, 2, 9, 4, 5, 0, 4, 11, 6]
# return {1, 9, 5, 11}


def maximum_sum(array, j):
    if j < 0:
        return 0

    take = array[j] + maximum_sum(array, j-2)
    dont_take = maximum_sum(array, j-1)
    return max(take, dont_take)


def dp_maximum_sum(array):
    l = len(array)
    cache = [0] * (l+1)
    for i in range(0, l):
        cache[i+1] = max(
            cache[i],
            cache[i-1] + array[i] if i - 2 >= 0 else array[i]
        )

    print(cache)




if __name__ == '__main__':
    print(maximum_sum(a, len(a)-1))
    print(dp_maximum_sum(a))