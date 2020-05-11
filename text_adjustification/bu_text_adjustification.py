from typing import List
text = "Tushar Ray likes to code".split()


"""
How you define badness

abs(max_line_width, line_width) ** 2

"""


def text_adjustification(text: List, max_line_width=10):
    n_words = len(text)
    # line_width determine the maximum number of words per line
    max_number_words_per_line = min(max_line_width // 2, n_words)
    cache = [[float('inf')] * max_number_words_per_line for _ in range(n_words)]

    for i, row in enumerate(cache):
        for j in range(i+1, i+1+max_number_words_per_line):
            if j > n_words:
                break
            line_width = len(" ".join(text[i:j]))
            if line_width > max_line_width:
                break
            row[j-1-i] = (max_line_width - line_width) ** 2

    for row in cache:
        print(row)

    cost_cache = [float('inf')] * (len(text) + 1)
    cost_cache[-1] = 0
    i = len(text) - 1
    while i > -1:
        row = cache[i]
        for k in range(min(len(text)-i, max_number_words_per_line)):
            cost = row[k]
            combined_cost = cost + cost_cache[i+k+1]
            if cost_cache[i] > combined_cost:
                cost_cache[i] = combined_cost

        i -= 1
    print(cost_cache)
    return cost_cache[0]

if __name__ == '__main__':
    print(text_adjustification(text))
