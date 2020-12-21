

text = "Tushar Ray likes to code".split()

print(text)


def text_adjustification(lst_words, line_width, k):
    if len(lst_words) < k+1:
        return 0, []
    min_cost = float('inf')
    min_solution = None
    for j in range(k+1, len(lst_words)+1):
        width = len(" ".join(lst_words[k:j]))
        if width >= line_width:
            break
        suffix_cost, suffix_solution = text_adjustification(lst_words, line_width, j)
        current_line_cost = (line_width-width) ** 2
        current_cost = suffix_cost + current_line_cost
        if current_cost < min_cost:
            min_cost = current_cost
            min_solution = [k] + suffix_solution
    return min_cost, min_solution


if __name__ == '__main__':
    print(text_adjustification(text, 10, 0))
