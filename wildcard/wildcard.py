ss = "xyxzzxy"
p = "x***y"
ss2 = "xyxzzxy"
p2 = "x***x"


def match(ss, p):
    res = False
    cache = [[0] * (len(ss)+1) for _ in range(len(p)+1)]
    for i in range(len(p)):
        for j in range(len(ss)):
            if p[i] == '*' or p[i] == ss[j]:
                cache[i+1][j+1] = cache[i][j] + 1
                if cache[i+1][j+1] == len(p):
                    res = True
    for row in cache:
        print(row)
    return res


if __name__ == '__main__':
    print(match(ss, p))
    print()
    print(match(ss2, p2))