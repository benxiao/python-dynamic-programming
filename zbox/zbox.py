import numba as nb
import numpy as np
concated = "abcxxxabyyy"

NumbaBytes = nb.typeof("".encode())
Numba1DInt64Array = nb.typeof(np.ones(1, dtype=np.uint32))
print(Numba1DInt64Array)


def navie_zbox(s):
    l = len(s)
    zs = [0] * l
    zs[0] = l
    for k in range(1, l):
        current_z = 0
        for j in range(l):
            if k + j < l and s[j] != s[k+j]:
                break
            current_z += 1
        zs[k] = current_z
    return zs


@nb.njit(Numba1DInt64Array(NumbaBytes))
def jit_zbox_algo(s):
    l = len(s)
    zs = np.zeros(l, dtype=nb.uint32)
    zs[0] = l
    left, right = 0, 0
    for k in range(1, l):
        # we are inside of the zbox
        if right >= k:
            # zval is contained in the zbox
            z_val = min(zs[k - left], l - k)
            if z_val + k <= right:
                zs[k] = z_val
            else:
                while k + z_val < l:
                    if s[z_val] != s[k + z_val]:
                        break
                    z_val += 1
                zs[k] = z_val
                left = k
                right = left + z_val - 1
        # we are outside of the zbox
        else:
            z_val = 0
            for i in range(l):
                if i + k >= l or s[i] != s[i + k]:
                    break
                z_val += 1
            zs[k] = z_val
            left = k
            right = left + z_val - 1

    return zs


def zbox_algo(s, debug=False):
    l = len(s)
    zs = [-1] * l
    zs[0] = l
    left, right = 0, 0
    for k in range(1, l):
        # we are inside of the zbox
        if debug:
            print(f"{k} iteration:")
            print(s)
            print(s[k:])

        if right >= k:
            # zval is contained in the zbox
            z_val = min(zs[k-left], l-k)
            if z_val + k <= right:
                zs[k] = min(z_val, l-k)
                if debug:
                    print(f"  zbox: ({left}, {right})")
                    print("  we are inside the zbox, no comparision needed")
                    print("  ", zs)
            else:
                z_val = min(zs[k-left], l-k)
                while k+z_val < l:
                    if s[z_val] != s[k+z_val]:
                        break
                    z_val += 1

                zs[k] = z_val
                left = k
                if z_val:
                    right = left + z_val - 1
                else:
                    right = left

                if debug:
                    print(f"  zbox: ({left}, {right})")
                    print("  we are extend outside the zbox, comparisons needed")
                    print("  ", zs)
        # we are outside of the zbox
        else:
            z_val = 0
            for i in range(l):
                if i+k >= l or s[i] != s[i+k]:
                    break
                z_val += 1
            zs[k] = z_val
            left = k
            if z_val:
                right = left + z_val - 1
            else:
                right = left
            if debug:
                print(f"  zbox: ({left}, {right})")
                print("  we are outside the zbox, manual comparsion needed")
                print("  ", zs)
    return zs









if __name__ == '__main__':
    a = "abcabcabc"
    print(zbox_algo(a, debug=True))
    b = "aabcaabxaaaz"
    print(zbox_algo(b, debug=True))
    print(jit_zbox_algo(a.encode()))