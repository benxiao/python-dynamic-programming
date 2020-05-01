from collections import Counter


def rec_permut(d, c, lst):
    if c == 0:
        print("".join(lst))

    for ch in d:
        if d[ch] > 0:
            d[ch] -= 1
            lst.append(ch)
            rec_permut(d, c-1, lst)
            d[ch] += 1
            lst.pop()


def permut(text):
    character_counter = Counter(text)
    text_length = len(text)
    stack = []
    charset = sorted(set(character_counter.keys()))
    stack.append(("", iter(charset)))
    while stack:
        sofar, it = stack[-1]
        try:
            while 1:
                ch = next(it)
                if character_counter[ch] > 0:
                    character_counter[ch] -= 1
                    break
            stack.append((sofar+ch, iter(charset)))

        except StopIteration:
            sofar, _ = stack.pop()
            if len(sofar) == text_length:
                yield sofar
            if len(sofar):
                character_counter[sofar[-1]] += 1


if __name__ == '__main__':
    #print(rec_permut({"a": 2, "b":1, "c": 1}, 4, []))
    for x in permut("davidson"):
        print(x)