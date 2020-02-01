
def dp_regex(pattern, source_string):
    sl, pl = len(source_string), len(pattern)
    cache = [[0] * (pl+1) for _ in range(sl+1)]

    for i in range(1, sl+1):
        cache[i][0] = 0

    for i in range(1, pl+1):
        cache[0][i] = 0

    # empty string matches empty pattern by definition
    cache[0][0] = 1

    for i in range(1, sl+1):
        for j in range(1, pl+1):
            # straight match
            if source_string[i-1] == pattern[j-1] or pattern[j-1] == '.':
                cache[i][j] = cache[i-1][j-1]
            if pattern[j-1] == '*':
                # zero occurences
                cache[i][j] = cache[i][j-2]
                # 1 or more occurences
                if source_string[i-1] == pattern[j-2] or pattern[j-2] == '.':
                    cache[i][j] = cache[i][j] or cache[i-1][j]
    for row in cache:
        print(row)

if __name__ == '__main__':
    print(dp_regex("ac*b", "accccccccccb"))
