"""
Find minimum number of deletions required to convert a string
into a palindrome

Given a string, find minimum number of deletions required
to convert it into palindrome
"""

s = "ACBCDBAA"


def mdtp(s, i, j):
    if i >= j:
        return 0

    if s[i] == s[j]:
        return mdtp(s, i+1, j-1)
    else:
        return 1 + min(mdtp(s, i+1, j), mdtp(s,i, j-1))



if __name__ == '__main__':
    print(mdtp(s, 0, len(s)-1))