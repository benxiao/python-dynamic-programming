
values = [60, 100, 120]
weights = [10, 20, 30]


def knapsack(values, weights, i, weight_limit):
    if i == -1:
        return 0

    if weights[i] > weight_limit:
        return knapsack(values, weights, i - 1, weight_limit)

    return max(knapsack(values, weights, i - 1, weight_limit),
               values[i] + knapsack(values, weights, i - 1, weight_limit - weights[i]))


def dp_knapsack(values, weights, weight_limit):
    cache = [[0] * (weight_limit+1) for _ in range(len(values)+1)]

    for i in range(len(values)):
        for j in range(1, weight_limit+1):
            if weights[i] > j:
                cache[i+1][j] = cache[i][j]
            else:
                cache[i+1][j] = max(
                    cache[i][j],
                    cache[i][j - weights[i]] + values[i]
                )
    print(cache)


if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [1, 2, 3]
    print(dp_knapsack(values, weights, 6))
    #print(knapsack(values, weights, len(values) - 1, 50))
