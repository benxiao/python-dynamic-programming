
dimensions = [(40, 20), (20, 30), (30, 10), (10, 30)]
symbols = ['A', 'B', 'C', 'D']
dimensions2 = [(10, 20), (20, 30), (30, 40), (40, 30)]


def opt(demensions, symbols):
    if len(demensions) == 1:
        return 0, symbols[0]
    minimum_ops = float('inf')
    minimum_str = ""
    for i in range(len(demensions) - 1):
        previous_solution, result_string = opt(
            demensions[:i] + [(demensions[i][0], demensions[i + 1][1])] + demensions[i + 2:],
            symbols[:i] + [f"({symbols[i]}{symbols[i+1]})"] + symbols[i+2:]
        )

        current_ops = demensions[i][0] * demensions[i + 1][0] * demensions[i + 1][1] + previous_solution
        if minimum_ops > current_ops:
            minimum_ops = current_ops
            minimum_str = result_string

    return minimum_ops, minimum_str


if __name__ == '__main__':
    print(opt(dimensions, symbols))
    print(opt(dimensions2, symbols))
