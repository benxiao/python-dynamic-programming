length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]


def rod_cutting(prices, lengths, n):
    cache = [0] * (n+1)
    for i in range(1, n+1):
        current_max = 0
        for l in lengths:
            if i - l >= 0:
                current = cache[i-l] + prices[l - 1]
                if current > current_max:
                    current_max = current
        cache[i] = current_max

    return cache[n]


length2price = {
    1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20
}


def rod_cutting2(length2price, n):
    cache = [0] * (n + 1)
    for i in range(1, n + 1):
        current_max = 0
        for l in length2price:
            if i - l >= 0:
                current = cache[i - l] + length2price[l]
                if current > current_max:
                    current_max = current
        cache[i] = current_max

    print(cache)
    return cache[n]


if __name__ == '__main__':
    print(rod_cutting2(length2price, 4))