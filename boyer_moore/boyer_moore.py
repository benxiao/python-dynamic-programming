"""
The Boyer-Moore Algorithm
Three ideas
Right-to left scan of the pattern at each possible alignment
Precompute R(x) to compute shifts when mismatches occur
Precompute L'(i) and l'(i) using suffix matches for further shifts
Definition: R(x) is the position of the rightmost occurrence of x in P (or zero)

Example: P = actca, so R(a) = 5, R(c) = 4, R(g) = 0, R(t) = 3

T = actgactaactca
P = actca
Bad character shift rule: If the first mismatch is found at position i (when scanning the pattern right to left) and T(k) is the text character that mismatches P(i), then shift the pattern right by max(1, i - R(T(k))

In the above example, i = k = 4 and T(k) = g, so the shift is 4 - R(g) = 4

Extended bad character shift rule: shift so that the next occurrence of T(k) in P (scanning left) is matched to T(k)
Preprocessing requires space proportional to the pattern length rather than the alphabet size
"""


def boyer_moore_preproc(strng):
    """
    space requirement, the size of the alphabet
    :param strng:
    :return:
    """
    d = {}
    for i, ch in enumerate(strng):
        d[ch] = i
    return d

def boyer_moore_extended_preproc(strng):
    """
    space requirement, the size of the pattern
    :param strng:
    :return:
    """


def search(needle, haystack, preproc):
    # implement bad character rule
    skip = preproc(needle)
    needle_length = len(needle)
    haystack_length = len(haystack)
    i = needle_length - 1
    while i < haystack_length:
        # right to left scanning on each alignment
        for (k, m) in zip(reversed(range(needle_length)), reversed(range(i+1))):
            if haystack[m] != needle[k]:
                skip_value = skip.tree_get(haystack[m])
                if skip_value is None:
                    i += needle_length
                else:
                    # print(haystack)
                    # print("i:", i)
                    # print("k:", k)
                    # print("skip:", k-skip_value)
                    # print()
                    # this is not done correctly
                    i += max(1, k-skip_value)
                break
        else:
            return i-needle_length+1
    return -1

