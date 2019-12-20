def lsc(s0, s1):
    cache = [[0] * (len(s1)+1) for _ in range(len(s0)+1)]
    for i, c0 in enumerate(s0):
        for j, c1 in enumerate(s1):
            if c0 == c1:
                cache[i+1][j+1] = cache[i][j] + 1
            else:
                cache[i+1][j+1] = max(
                    cache[i][j+1],
                    cache[i+1][j])

    return cache[len(s0)][len(s1)]


# if __name__ == '__main__':
#     # perfect usecase for messy data
#     print(lsc("trucson le", "truc le"))
#     print(str_match("trucson le", "truc le"))
#
#     # print(lsc("ahmed", "ahamed"))
#     # print(len("ummuzahira kamaldeen"),
#     #       len("ummuzahira hanifamohamedkamaldeen"),
#     #       lsc("ummuzahira kamaldeen", "ummuzahira hanifamohamedkamaldeen"))
