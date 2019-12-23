"""
Check if given string is interleaving of two other given strings
Given three strings, return true if third string is interleaving
of first and second strings. ie, it is formed from all characters
of first and second string and order of characers is preserved

For example,
ACDB is interleaving of AB and CD
ADEBCF is interleaving of ABC and DEF
"""


def is_interleaving(source, a, b, k, i, j):
    if k == -1:
        return True
    if i > -1 and source[k] == a[i] :
        return is_interleaving(source, a, b, k-1, i-1, j)
    elif j > -1 and source[k] == b[j]:
        return is_interleaving(source, a, b, k-1, i, j-1)
    else:
        return False


def is_interleaving_iterative(source, a, b):
    i, j, k = 0, 0, 0
    if len(source) != len(a) + len(b):
        return False

    while k < len(source):
        if i < len(a) and source[k] == a[i]:
            i += 1
            k += 1
        elif j < len(b) and source[k] == b[j]:
            j += 1
            k += 1
        else:
            return False

    return True


if __name__ == '__main__':
    print(is_interleaving("ACDB", "AB", "CD", 3, 1, 1))
    print(is_interleaving("ACDABC", "ABC", "ACD", 5, 2, 2))
