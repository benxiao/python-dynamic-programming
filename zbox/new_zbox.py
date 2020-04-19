original_str = "aabxaabxcaabxaabxay"

z_values = [0, 1, 0, 0, 4, 1, 0, 0, 0, 8, 1, 0, 0, 5, 1, 0, 0, 1, 0]


def z_algo(source):
    source_length = len(source)
    z_values = [0] * source_length
    left, right = 0, 0
    for k in range(1, source_length):
        # we do str cmp
        if k >= right:
            left = right = k
            for i, j in enumerate(range(k, source_length)):
                if source[i] != source[j]:
                    break
                right += 1

            z_values[k] = right - left

        # we may use the precomputed results
        else:
            z_value = z_values[k-left]
            # we stay within the current zbox
            if k + z_value < right:
                z_values[k] = z_value

            # we extend outside the current zbox
            else:
                # length within the zbox
                length = right - k
                while k+length < source_length:
                    if source[length] != source[k+length]:
                        break
                    length += 1
                z_values[k] = length
                left = k
                right = left + length
    return z_values

# print(z_values)
# print(z_algo(original_str))


