dictionary = {'I', 'a', 'am', "bad", "ass", "badass"}


def word_break(dictionary, text):
    l = len(text)
    cache = [[0] * l for _ in range(l)]
    word_cache = [[None for _ in range(l)] for _ in range(l)]
    for step in range(l):
        for start in range(l - step):
            start, end = start, start + step
            cache[start][end] = int(text[start: end+1] in dictionary)
            if cache[start][end]:
                word_cache[start][end] = [text[start:end+1]]
            else:
                for split in range(start+1, end+1):
                    if cache[start][split-1] and cache[split][end]:
                        cache[start][end] = 1
                        word_cache[start][end] = word_cache[start][split-1] + word_cache[split][end]

    print(cache)
    print(word_cache)

    return word_cache[0][-1]



print(word_break(dictionary, "abadass"))
