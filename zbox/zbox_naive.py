from typing import *

original_str = "aabxaabxcaabxaabxay"


def naive_z_algo(original_str) -> List[int]:
    str_length = len(original_str)
    z_values = [0] * str_length
    for k in range(1, str_length):
        for i, j in enumerate(range(k, str_length)):
            if original_str[i] != original_str[j]:
                z_values[k] = i
                break
        else:
            z_values[k] = i+1

    return z_values


"""
[0,1,2,3,4,5 ...]
[a,b,c,$,a,b ...]
"""


def search(haystack: str, needle: str, algo: Callable[[str], List[int]]) -> List[int]:
    z_str = needle + "$" + haystack
    z_values = algo(z_str)
    needle_length = len(needle)
    z_str_length = len(z_str)
    result = []
    offset = len(needle) + 1  # 1 counts for "$"
    for i in range(offset, z_str_length):
        if z_values[i] == needle_length:
            result.append(i - offset)
    return result


if __name__ == '__main__':
    print(naive_z_algo(original_str))