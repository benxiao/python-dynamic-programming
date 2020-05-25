def palindrome(text):
    str_length = len(text)
    cache = [0] * str_length
    cache[0] = 0
    right = 0
    mid = 0
    for i in range(1, str_length):
        if right < i:
            k = 1
            while i-k >= 0 and i+k < str_length and text[i-k] == text[i+k]:
                k += 1
            cache[i] = k-1
            right = i+k-1
            mid = i
        else:
            length = cache[mid-(i-mid)]
            if i + length < right:
                cache[i] = length
            else:
                length = right - i
                k = 1
                while right + k < str_length and i - length - k >= 0 and text[right+k] == text[i-length-k]:
                    k += 1

                cache[i] = length + k - 1
                right += k-1
                mid = i

        print([x*2+1 for x in cache])


if __name__ == '__main__':
    palindrome("abaxabaxabb")