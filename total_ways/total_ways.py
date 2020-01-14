"""
** Coin change problem (total number of ways to get the denomination of coins **

Given an unlimited supply of coins of given denominations, find the total number of
distinct ways to get a desired change.
"""



lst = [1, 3, 5, 7]
import bisect


def total(n, lst, i):
    if n == 0:
        return [[]]
    result = []
    for k in range(i, len(lst)):
        if n-lst[k] >= 0:
            prev_result = total(n-lst[k], lst, k)
            for item in prev_result:
                item.append(lst[k])
            result.extend(prev_result)
    return result


def dp_total(n, lst):
    cache = [0] * (n+1)
    cache[0] = 1
    cache_items = [[] for _ in range(n+1)]
    cache_items[0].append([])
    for k in range(1, n+1):
        for c in lst:
            if k - c >= 0:
                for e in cache_items[k - c]:
                    if e and e[-1] > c:
                        continue
                    cache_items[k].append([*e, c])
                    cache[k] += 1

    return cache, cache_items

print(dp_total(8, lst))

#
#
#
# def insertion_sort(lst):
#     for i in range(1, len(lst)):
#         j = i - 1
#         v = lst[i]
#         while j >= 0 and lst[j] > v:
#             j -= 1
#         lst[j+2: i+1] = lst[j+1: i]
#         lst[j+1] = v
#     return lst
#
#
# """
# Binary Insertion sort is a special type up of Insertion sort which uses binary search algorithm to find out the correct position of the inserted element in the array.
#
# Insertion sort is sorting technique that works by finding the correct position of the element in the array and then inserting it into its correct position.
#
# Binary search is searching technique that works by finding the middle of the array for finding the element.
#
# As the complexity of binary search is of logarithmic order, the searching algorithm’s time complexity will also decrease to of logarithmic order.
#
# Implementation of binary Insertion sort. this program is a simple Insertion sort program but instead of the standard searching technique binary search is used.
# """
#
#
#
# def bisort(lst):
#     for i in range(1, len(lst)):
#         v = lst[i]
#         j = bisect.bisect_right(lst, v, 0, i)
#         lst[j+1:i+1] = lst[j:i]
#         lst[j] = v
#
# a = "abc"
#
#
#
#
# """
# The Boyer-Moore Algorithm
# Three ideas
# Right-to left scan of the pattern at each possible alignment
# Precompute R(x) to compute shifts when mismatches occur
# Precompute L'(i) and l'(i) using suffix matches for further shifts
# Definition: R(x) is the position of the rightmost occurrence of x in P (or zero)
#
# Example: P = actca, so R(a) = 5, R(c) = 4, R(g) = 0, R(t) = 3
#
# T = actgactaactca
# P = actca
# Bad character shift rule: If the first mismatch is found at position i (when scanning the pattern right to left) and T(k) is the text character that mismatches P(i), then shift the pattern right by max(1, i - R(T(k))
#
# In the above example, i = k = 4 and T(k) = g, so the shift is 4 - R(g) = 4
#
# Extended bad character shift rule: shift so that the next occurrence of T(k) in P (scanning left) is matched to T(k)
# Preprocessing requires space proportional to the pattern length rather than the alphabet size
# """
#
#
# def boyer_moore_preproc(strng):
#     """
#     space requirement, the size of the alphabet
#     :param strng:
#     :return:
#     """
#     d = {}
#     for i, ch in enumerate(strng):
#         d[ch] = i
#     return d
#
# def boyer_moore_extended_preproc(strng):
#     """
#     space requirement, the size of the pattern
#     :param strng:
#     :return:
#     """
#
#
# def search(needle, haystack, preproc):
#     # implement bad character rule
#     skip = preproc(needle)
#     needle_length = len(needle)
#     haystack_length = len(haystack)
#     i = needle_length - 1
#     while i < haystack_length:
#         # right to left scanning on each alignment
#         for (k, m) in zip(reversed(range(needle_length)), reversed(range(i+1))):
#             if haystack[m] != needle[k]:
#                 skip_value = skip.get(haystack[m])
#                 if skip_value is None:
#                     i += needle_length
#                 else:
#                     # print(haystack)
#                     # print("i:", i)
#                     # print("k:", k)
#                     # print("skip:", k-skip_value)
#                     # print()
#                     # this is not done correctly
#                     i += max(1, k-skip_value)
#                 break
#         else:
#             return i-needle_length+1
#     return -1
#
#
#
# if __name__ == '__main__':
#     print(search("->", "acca->abc"))
#
#
