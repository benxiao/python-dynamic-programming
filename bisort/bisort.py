"""
Binary Insertion sort is a special type up of Insertion sort which uses binary search algorithm to find out the correct position of the inserted element in the array.

Insertion sort is sorting technique that works by finding the correct position of the element in the array and then inserting it into its correct position.

Binary search is searching technique that works by finding the middle of the array for finding the element.

As the complexity of binary search is of logarithmic order, the searching algorithm’s time complexity will also decrease to of logarithmic order.

Implementation of binary Insertion sort. this program is a simple Insertion sort program but instead of the standard searching technique binary search is used.
"""
import bisect


def bisort(lst):
    for i in range(1, len(lst)):
        v = lst[i]
        j = bisect.bisect_right(lst, v, 0, i)
        lst[j+1:i+1] = lst[j:i]
        lst[j] = v
