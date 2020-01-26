"""
Input: p[] = {40, 20, 30, 10, 30}
  Output: 26000
  There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
  Let the input 4 matrices be A, B, C and D.  The minimum number of
  multiplications are obtained by putting parenthesis in following way
  (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

  Input: p[] = {10, 20, 30, 40, 30}
  Output: 30000
  There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30.
  Let the input 4 matrices be A, B, C and D.  The minimum number of
  multiplications are obtained by putting parenthesis in following way
  ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30
"""
dimensions = [(40, 20), (20, 30), (30, 10), (10, 30)]
symbols = ['A', 'B', 'C', 'D']
dimensions2 = [(10, 20), (20, 30), (30, 40), (40, 30)]


def opt(demensions, symbols):

    assert len(dimensions) == len(symbols)

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
