from typing import *


class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return self.key == other.key

    def is_leave(self):
        return self.left is None and self.right is None

    def __str__(self):
        if self is None: return '<empty tree>'

        def recurse(node):
            if node is None: return [], 0, 0
            label = str((node.key, node.height))
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
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

    y.height = height(y)
    x.height = height(x)
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


def delete_min(tree):
    if tree.left is None:
        return tree.right
    tree.left = delete_min(tree.left)
    tree.height = height(tree)
    return apply_avl_rebalance(tree)


def delete_max(tree):
    if tree.right is None:
        return tree.left
    tree.right = delete_max(tree.right)
    tree.height = height(tree)
    return apply_avl_rebalance(tree)


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
    cur = tree
    while cur:
        if val < cur.val:
            cur = cur.left

        elif val > cur.val:
            prev = cur
            cur = cur.right
        else:
            break
    return prev


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


def apply_avl_rebalance(tree):
    if height(tree.left) > height(tree.right) + 1:
        if height(tree.left.left) > height(tree.left.right):
            tree = rotate_right(tree)
        else:
            tree.left = rotate_left(tree.left)
            tree = rotate_right(tree)

    elif height(tree.left) + 1 < height(tree.right):
        if height(tree.right.right) > height(tree.right.left):
            tree = rotate_left(tree)
        else:
            tree.right = rotate_right(tree.right)
            tree = rotate_left(tree)
    return tree


def insert(tree: TreeNode, key, val):
    if tree is None:
        return TreeNode(key, val)

    if key < tree.key:
        tree.left = insert(tree.left, key, val)
        tree.height = height(tree)
    else:
        tree.right = insert(tree.right, key, val)
        tree.height = height(tree)

    return apply_avl_rebalance(tree)


def tree_remove(tree: TreeNode, val: Any):
    if tree is None:
        return None
    if val < tree.key:
        tree.left = tree_remove(tree, val)
    elif val > tree.key:
        tree.right = tree_remove(tree, val)
    else:
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left

    # toDo


def tree_equal(tree0: TreeNode, tree1: TreeNode) -> bool:
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
        return btree_complete(tree.left, 2 * idx, count) \
               and btree_complete(tree.right, 2 * idx + 1, count)


def btree_count(tree):
    if tree is None:
        return 0
    return 1 + btree_count(tree.left) + btree_count(tree.right)


def check_avl_invariants(tree):
    if tree is None:
        return True
    if abs(height(tree.left) - height(tree.right)) > 1:
        return False

    return check_avl_invariants(tree.left) and check_avl_invariants(tree.right)


def check_heights(tree):
    if tree is None:
        return True
    if tree.height != max(height(tree.left), height(tree.right)) + 1:
        return False
    return check_heights(tree.left) and check_heights(tree.right)


class AVLTreeMap:
    def __init__(self, iterable: Dict = None):
        self.tree = None
        if not iterable:
            return

        for k, v in iterable.items():
            self.tree = insert(self.tree, k, v)

    def __bool__(self):
        return self.tree is not None

    def add(self, key, val):
        self.tree = insert(self.tree, key, val)

    def __str__(self):
        if self.tree is None:
            return "<empty>"
        return str(self.tree)

    def min(self):
        if self.tree is None:
            raise ValueError()
        return min_node(self.tree).val

    def max(self):
        if self.tree is None:
            raise ValueError()
        return max_node(self.tree).val

    def next_large(self, key):
        n = next_node(self.tree, key)
        if n is None:
            return n
        return n.val

    def prev(self, key):
        n = prev_node(self.tree, key)
        if n is None:
            return n
        return n.val

    def __len__(self):
        return btree_count(self.tree)

    def __eq__(self, other):
        if not isinstance(other, AVLTreeMap):
            return False

        return tree_equal(self.tree, other.tree)

    def delete_min(self):
        self.tree = delete_min(self.tree)

    def invariant_check(self):
        heights_ok = check_heights(self.tree)
        return heights_ok and check_avl_invariants(self.tree)


if __name__ == '__main__':
    root = None
    import random

    random.seed(0)
    tree = AVLTreeMap()
    for i in zip(range(20)):
        tree.add(random.randint(0, 1000), 1)
        print(tree)
        print()
        if not tree.invariant_check():
            raise ValueError("invariant check failed")

    while tree:
        tree.delete_min()
        print(tree)
        if not tree.invariant_check():
            raise ValueError("invariant check failed")
        print(end='\n' * 2)

    # root = tree.tree
    # root = delete_min(root)
    # print(root)
    # print()
    # root = delete_min(root)
    # print(root)
    # print()

    # key = tree.min()
    # while 1:
    #     print(key)
    #     key = tree.next_large(key)
    #     if key is None:
    #         break
    #
    # key = tree.max()
    # while 1:
    #     print(key)
    #     key = tree.prev(key)
    #     if key is None:
    #         break
    # print(len(tree))