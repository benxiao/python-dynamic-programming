"""
Calculate sum of all elements in a sub-matrix in constant time
Given a M * N matrix and two coordinates (p, q) and (r,s), which
represents top-left and bottom-right coordinates of a sub-matrix of
the given matrix, calculate the sum of all elements present in the
sub-matrix
"""

class FastSum1d:
    def __init__(self, lst):
        cache = lst.copy()
        for i in range(1, len(lst)):
            cache[i] += cache[i-1]
        self.cache = cache

    def get(self, start, stop):
        assert 0 <= start < len(self.cache)
        assert 0 <= stop < len(self.cache)
        return (self.cache[stop-1] if stop > 0 else 0) -\
               (self.cache[start-1] if start > 0 else 0)



class FastSum2d:
    def __init__(self, lst):
        self.rows = len(lst)
        self.cols = len(lst[0])
        self.cache = [[0] * self.cols for _ in range(self.rows)]
        self._preproc(lst)

    def _preproc(self, lst):
        for i in range(self.rows):
            self.cache[i][0] = lst[i][0]

        for i in range(1, self.rows):
            self.cache[i][0] += self.cache[i - 1][0]

        for i in range(self.cols):
            self.cache[0][i] = lst[0][i]

        for i in range(1, self.cols):
            self.cache[0][i] += self.cache[0][i - 1]

        for i in range(1, self.rows):
            for j in range(1, self.cols):
                self.cache[i][j] = self.cache[i - 1][j] +\
                                   self.cache[i][j - 1] -\
                                   self.cache[i - 1][j - 1] +\
                                   lst[i][j]

    def get(self, top_left, bottom_right):
        tl_r, tl_c = top_left # [)
        br_r, br_c = bottom_right # [)
        assert tl_r >= 0 and tl_c >= 0
        assert br_r >= 0 and br_c >= 0

        assert tl_r < self.rows and br_r < self.rows
        assert tl_c < self.cols and br_c < self.cols

        assert br_r >= tl_r
        assert br_c >= tl_c

        return self.cache[br_r-1][br_c-1] -\
        (self.cache[br_r-1][tl_c-1] if tl_r > 0 else 0) -\
        (self.cache[tl_r-1][br_c-1] if tl_c > 0 else 0) +\
        (self.cache[tl_r-1][tl_c-1] if tl_r > 0 and tl_c> 0 else 0)

    def __getitem__(self, slice_tuple):
        if len(slice_tuple) != 2:
            raise ValueError("takes two slices")
        row_slice, column_slice = slice_tuple
        if row_slice.step or column_slice.step:
            raise NotImplementedError("step is not supported")

        rs = row_slice.start or 0
        re = row_slice.stop or self.rows
        cs = column_slice.start or 0
        ce = column_slice.stop or self.cols
        return self.get((rs, cs), (re, ce))




if __name__ == '__main__':
    lst = [
        [0, 2, 5, 4, 1],
        [4, 8, 2, 3, 7],
        [6, 3, 4, 6, 2],
        [7, 3, 1, 8, 3],
        [1, 5, 7, 9, 4]
    ]

    fs = FastSum2d(lst)
    print(fs.get((0,0), (2, 2)))

    print(fs[2:2, 2:2])
    print(fs[:2, :2])

    fs1d = FastSum1d([1,2,3,4,5])
    print(fs1d.get(0,4))