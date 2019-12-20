"""
Longest repeated sequence

"""


seq = "ATACTCGGA"



def navie_lrs(seq, i, j):
    if i < 0 or j < 0:
        return 0

    if i!=j and seq[i] == seq[j]:
        return navie_lrs(seq, i-1, j-1) + 1

    return max(navie_lrs(seq, i-1, j), navie_lrs(seq, i,j-1))



if __name__ == '__main__':
    print(navie_lrs(seq, len(seq)-1, len(seq)-1))
