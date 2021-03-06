"""
Longest Alternating Subsequence is a problem of finding a subsequence
of a given sequence in which the elements are in alternating order,
and in which the sequence is as long as possible
"""

seq = [8, 9, 6, 4, 5, 7, 3, 2, 4]


# solution [8, 9, 6, 7, 2, 4]
def r_las(seq, j, f):
    if j < 0:
        return 0, []

    best_res, best_lst = 0, []
    for i in range(j):
        if f and seq[i] < seq[j]:
            res, lst = r_las(seq, i, not f)
            if res + 1 > best_res:
                best_res = res + 1
                best_lst = lst + [seq[i]]

        elif not f and seq[i] > seq[j]:
            res, lst = r_las(seq, i, not f)
            if res + 1 > best_res:
                best_res = res + 1
                best_lst = lst + [seq[i]]

        res, lst = r_las(seq, i, f)
        if res > best_res:
            best_res = res
            best_lst = lst

    return best_res, best_lst


def las(seq):
    last_idx = len(seq) - 1
    set_true = r_las(seq, last_idx, True)
    set_false = r_las(seq, last_idx, False)
    if set_true[0] > set_false[0]:
        return set_true
    return set_false


if __name__ == '__main__':
    print(las(seq))
