import math

arr = [-1, 2, 4, 0]

length_segment_tree = 2 ** math.ceil(math.log(len(arr))+1)


segment_tree = [float('inf')] * length_segment_tree
segment_tree[0] = None


def construct_segment_tree(arr, segment_tree, left, right, n):
    mid = (left + right) // 2
    if abs(left - right) == 1:
        segment_tree[n] = arr[left]
    else:
        construct_segment_tree(arr, segment_tree, left, mid, n << 1)
        construct_segment_tree(arr, segment_tree, mid, right, (n << 1) + 1)
        segment_tree[n] = min(segment_tree[n << 1], segment_tree[(n << 1) + 1])


def range_query(segment_tree, query_left, query_right, left, right, n):
    """
    partial overlap  query ( 3, 5 ), range( 2, 6), recurse
    total overlap return value from segment_tree
    no overlap return float('inf')
    """
    # total overlap
    if left >= query_left and right <= query_right:
        return segment_tree[n]
    # no overlap
    elif query_left >= right or left >= query_right:
        return float('inf')
    else:
        mid = (left + right) // 2
        return min(range_query(segment_tree, query_left, query_right, left, mid, n << 1),
                   range_query(segment_tree, query_left, query_right, mid, right, (n << 1)+1))




if __name__ == '__main__':
    construct_segment_tree(arr, segment_tree, 0, len(arr), 1)
    print(segment_tree)
    print(range_query(segment_tree, 1, 3, 0, 4, 1))
