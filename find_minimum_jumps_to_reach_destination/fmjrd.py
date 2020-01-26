"""
Find minimum jumps required to reach the destination

We have an array of non-negative integers, such that each element in
the array represents the maximum number of positions one can move forward
from that position. Find the minimum number of jumps required to reach to
reach the given destination from the given source within the array.
"""


a0 = [4, 2, 2, 1, 0, 8, 1]
a1 = [4, 2, 0, 3, 2, 0, 1, 8]


def minimum_jumps(a, start, end):
    if start == end:
        return 0
    current_jumps = a[start]
    result = float('inf')
    for i in range(1, current_jumps+1):
        if start+i <= end:
            result = min(result, minimum_jumps(a, start+i, end)+1)
    return result


def dp_minimum_jumps(a):
    pass



if __name__ == '__main__':
    print(minimum_jumps(a0, 0, len(a0)-1))
    print(minimum_jumps(a1, 0, len(a1)-1))