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
from functools import reduce

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
            symbols[:i] + [f"({symbols[i]}{symbols[i + 1]})"] + symbols[i + 2:]
        )

        current_ops = demensions[i][0] * demensions[i + 1][0] * demensions[i + 1][1] + previous_solution
        if minimum_ops > current_ops:
            minimum_ops = current_ops
            minimum_str = result_string

    return minimum_ops, minimum_str


shapes1 = [40, 20, 30, 10, 30]
# symbols = [None, 'A', 'B', 'C', 'D']
shapes2 = [10, 20, 30, 40, 30]


def opt2(shapes, i, j):
    if i == j:
        return 0
    minimum_ops = float('inf')
    for k in range(i, j):

        count = opt2(shapes, i, k) + opt2(shapes, k + 1, j) + shapes[i - 1] * shapes[k] * shapes[j]

        if count < minimum_ops:
            minimum_ops = count
            minimum_conf = (shapes[i - 1], shapes[k], shapes[j])
    # print(f"called ({i}, {j})")
    print(minimum_conf)

    return minimum_ops



def dp_opt(shapes, symbols):
    # number of matrixes
    n = len(shapes)
    cache = [[0] * n for _ in range(n)]
    expression_cache = [[""] * n for _ in range(n)]
    for i in range(n - 2):
        cache[i][i + 2] = shapes[i] * shapes[i+1] * shapes[i+2]
        expression_cache[i][i + 2] = f"{symbols[i]}{symbols[i + 1]}"

    for k in range(3, n):
        for start in range(n - k):
            end = start + k
            minimum_ops = float('inf')
            for i in range(start + 1, end):
                current_ops = cache[start][i] + shapes[start] * shapes[i] * shapes[end] + cache[i][end]

                if current_ops < minimum_ops:
                    minimum_ops = current_ops
                    if expression_cache[start][i] is "":
                        expression_cache[start][end] = f"{symbols[start]}({expression_cache[i][end]})"
                    if expression_cache[i][end] is "":
                        expression_cache[start][end] = f"({expression_cache[start][i]}){symbols[end - 1]}"

            cache[start][end] = minimum_ops

    # for row in cache:
    #     print(row)
    #
    # for row in expression_cache:
    #     print(row)
    return cache[0][-1], expression_cache[0][-1]


if __name__ == '__main__':
    print(dp_opt(shapes1, symbols))
    print(dp_opt(shapes2, symbols))
# print(mult([1,2,3]))

"""
(0, 0) (0, 1) (0, 2) (0, 3)
       (1, 1) (1, 2) (1, 3)
              (2, 2) (2, 3)
                     (3, 3)
                      
    ab  abc
0 0 x x
  0 0 x bc
    0 0
      0 
"""
