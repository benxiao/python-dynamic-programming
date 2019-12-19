from typing import *


def coins(n: int, choices: List):
    array = [0] * (n+1)
    for i in range(1, n+1):
        min_l = n  # worst case and used it as a placeholder
        for choice in choices:
            if i-choice >= 0:
                if array[i-choice] + 1 < min_l:
                    min_l = array[i-choice] + 1
        array[i] = min_l
    return array[n]


def coins_opt(n: int, choices: List):
    array = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        min_l, items = n, []
        for choice in choices:
            if i - choice >= 0:
                if len(array[i-choice]) + 1 < min_l:
                    min_l = len(array[i-choice]) + 1
                    items = array[i-choice] + [choice] # this creates a list, so don't worry
        array[i] = items
    return array[n]


if __name__ == '__main__':
    print(coins_opt(101, [1, 2, 5, 10]))
