s = "BABABCBADCD"


def is_palindrome(x, i, j):
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True


# this problem is very similiar to perfect BST or longest palindrome problem
def min_cut(x, i, j):
    if i >= j or is_palindrome(x, i, j):
        return 0
    min_val = len(x)
    for k in range(i, j):
        current = min_cut(x, i, k) + 1 + min_cut(x, k+1, j)
        min_val = min(min_val, current)
    return min_val


if __name__ == '__main__':
    # assert min_cut(s, 0, len(s)-1) == 2
    # assert min_cut("ABCBA", 0, 4) == 0
    print(min_cut("ABCD", 0, 3))