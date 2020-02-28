from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val

    def __str__(self):
        if self is None: return '<empty tree>'

        def recurse(node):
            if node is None: return [], 0, 0
            label = str((node.val, node.height))
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            # if (middle - len(label)) % 2 == 1 and node.parent is not None and \
            #         node is node.parent.left and len(label) < middle:
            #     label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        return '\n'.join(recurse(self)[0])


def rotate_right(y):
    x = y.left
    t1 = x.left
    t2 = x.right
    t3 = y.right

    x.left = t1
    x.right = y
    y.left = t2
    y.right = t3

    x.height = height(x)
    y.height = height(y)
    return x


def rotate_left(x):
    y = x.right
    t1 = x.left
    t2 = y.left
    t3 = y.right

    y.left = x
    y.right = t3
    x.left = t1
    x.right = t2

    x.height = height(x)
    y.height = height(y)

    return y


def height(tree):
    if tree is None:
        return 0
    left = tree.left.height if tree.left else 0
    right = tree.right.height if tree.right else 0
    return max(left, right) + 1


def delete(tree, val):
    node = get(tree, val)
    pass


def min_node(tree):
    cur = tree
    if cur is None:
        return cur
    while cur.left:
        cur = cur.left
    return cur


def max_node(tree):
    cur = tree
    if cur is None:
        return cur
    while cur.right:
        cur = cur.right
    return cur


def get(tree, val):
    if tree is None:
        raise KeyError()

    cur = tree
    while cur:
        if val < cur.val:
            cur = cur.left

        elif val > cur.val:
            cur = cur.right

        else:
            return cur
    raise KeyError()


def prev_node(tree, val):
    target = get(tree, val)
    if target.left:
        return max_node(target.left)
    prev = None
    # prev_node is the parent node of target node




def next_node(tree, val):
    target = get(tree, val)
    if target.right:
        return min_node(target.right)

    # next_node is the parent node of target node
    # target_node is guaranteed to be the left child of next_node
    succ = None
    cur = tree
    while cur:
        if val < cur.val:
            succ = cur
            cur = cur.left

        elif val > cur.val:
            cur = cur.right
        else:
            break
    return succ


def insert(tree, val):
    if tree is None:
        return TreeNode(val)

    if val < tree.val:
        tree.left = insert(tree.left, val)
        tree.height = height(tree)
    else:
        tree.right = insert(tree.right, val)
        tree.height = height(tree)

    if height(tree.left) > height(tree.right)+1:
        if height(tree.left.left) > height(tree.left.right):
            tree = rotate_right(tree)
            tree.height = height(tree)
        else:
            tree.left = rotate_left(tree.left)
            tree.left.height = height(tree.left)

            tree = rotate_right(tree)
            tree.height = height(tree)

    elif height(tree.left)+1 < height(tree.right):
        if height(tree.right.right) > height(tree.right.left):
            tree = rotate_left(tree)
            tree.height = height(tree)
        else:
            tree.right = rotate_right(tree.right)
            tree.right.height = height(tree.right)

            tree = rotate_left(tree)
            tree.height = height(tree)

    return tree


def tree_equal(tree0: TreeNode, tree1: TreeNode)->bool:
    if tree0 != tree1:
        return False
    left, right = True, True
    if tree0.left or tree1.left:
        left = tree_equal(tree0.left, tree1.left)
    if tree0.right or tree1.right:
        right = tree_equal(tree0.right, tree1.right)
    return left and right


def btree_complete(tree, idx, count):
    if tree is None:
        return True

    elif idx > count:
        return False

    else:
        return btree_complete(tree.left, 2*idx, count) \
            and btree_complete(tree.right, 2*idx+1, count)


def btree_count(tree):
    if tree is None:
        return 0
    return 1 + btree_count(tree.left) + btree_count(tree.right)




if __name__ == '__main__':
    root = None
    import random
    random.seed(0)
    for i in zip(range(20)):
        root = insert(root, random.randint(1, 1000))
        print()
        print(root)

    print()
    print(get(root, 989))


    print(min_node(root))
    print(next_node(root, 914))