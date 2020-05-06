import numba as nb
import numpy as np


def robin_karp2(text, pattern):
    length_text = len(text)
    length_pattern = len(pattern)
    prime = 83921
    hash_pattern = 0
    hash_text = 0
    d = 256
    h = pow(d, length_pattern - 1, prime)

    for x, y in zip(pattern, text):
        hash_pattern = (hash_pattern * d + ord(x)) % prime
        hash_text = (hash_text * d + ord(y)) % prime

    result = []
    i, j = 0, length_pattern
    while 1:
        #print(hash_text)
        if hash_text == hash_pattern:
            for ii, jj in zip(range(length_pattern), range(i, i+length_pattern)):
                if pattern[ii] != text[jj]:
                    break
            else:
                result.append(i)

        if j == length_text:
            break

        # sliding
        hash_text = ((hash_text - h * ord(text[i])) * d + ord(text[j])) % prime
        i += 1
        j += 1

    return result


def robin_karp(text, pattern):
    prime = 101
    length_text = len(text)
    length_pattern = len(pattern)
    hash_pattern = sum(ord(x) * (prime ** i) for i, x in enumerate(pattern))
    #print(hash_pattern)

    hash_text = sum(ord(x) * (prime ** i) for i, x in enumerate(text[:length_pattern]))
    #print(hash_text)

    result = []
    i, j = 0, length_pattern
    while 1:

        if hash_text == hash_pattern:
            for ii, jj in zip(range(length_pattern), range(i, i+length_pattern)):
                if pattern[ii] != text[jj]:
                    break
            else:
                result.append(i)

        if j == length_text:
            break

        # sliding
        hash_text = (hash_text - ord(text[i])) // prime + (prime ** (length_pattern-1) * ord(text[j]))
        i += 1
        j += 1

    return result

