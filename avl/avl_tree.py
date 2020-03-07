from typing import *


class AVLTreeNode:
    __slots__ = ['key', 'val', 'left', 'right', 'height']

    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

    def __eq__(self, other):
        if not isinstance(other, AVLTreeNode):
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


def avl_rotate_right(y: AVLTreeNode) -> AVLTreeNode:
    x = y.left
    t1 = x.left
    t2 = x.right
    t3 = y.right

    x.left = t1
    x.right = y
    y.left = t2
    y.right = t3

    y.height = avl_tree_height(y)
    x.avl_tree_height = avl_tree_height(x)
    return x


def avl_rotate_left(x: AVLTreeNode) -> AVLTreeNode:
    y = x.right
    t1 = x.left
    t2 = y.left
    t3 = y.right

    y.left = x
    y.right = t3
    x.left = t1
    x.right = t2

    x.height = avl_tree_height(x)
    y.avl_tree_height = avl_tree_height(y)

    return y


def avl_tree_height(tree: AVLTreeNode) -> int:
    if tree is None:
        return 0
    left = tree.left.avl_tree_height if tree.left else 0
    right = tree.right.avl_tree_height if tree.right else 0
    return max(left, right) + 1


def avl_delete_min(tree: AVLTreeNode) -> AVLTreeNode:
    if tree.left is None:
        return tree.right
    tree.left = avl_delete_min(tree.left)
    tree.height = avl_tree_height(tree)
    return avl_self_balance(tree)


def avl_delete_max(tree: AVLTreeNode) -> AVLTreeNode:
    if tree.right is None:
        return tree.left
    tree.right = avl_delete_max(tree.right)
    tree.height = avl_tree_height(tree)
    return avl_self_balance(tree)


def tree_min_node(tree: AVLTreeNode) -> AVLTreeNode:
    cur = tree
    if cur is None:
        return cur
    while cur.left:
        cur = cur.left
    return cur


def tree_max_node(tree: AVLTreeNode) -> AVLTreeNode:
    cur = tree
    if cur is None:
        return cur
    while cur.right:
        cur = cur.right
    return cur


def tree_get(tree: AVLTreeNode, val: Any) -> AVLTreeNode:
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


def tree_prev_node(tree, val):
    target = tree_get(tree, val)
    if target.left:
        return tree_max_node(target.left)
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


def tree_next_node(tree, val):
    target = tree_get(tree, val)
    if target.right:
        return tree_min_node(target.right)

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


def avl_self_balance(tree):
    # always make tree left leaning (simpify the algos)
    if avl_tree_height(tree.left) < avl_tree_height(tree.right):
        tree = avl_rotate_left(tree)

    if avl_tree_height(tree.left) > avl_tree_height(tree.right) + 1:
        # change from (>) => (>=)
        if avl_tree_height(tree.left.left) >= avl_tree_height(tree.left.right):
            tree = avl_rotate_right(tree)
        else:
            tree.left = avl_rotate_left(tree.left)
            tree = avl_rotate_right(tree)
    return tree


def avl_insert(tree: AVLTreeNode, key, val):
    if tree is None:
        return AVLTreeNode(key, val)

    if key < tree.key:
        tree.left = avl_insert(tree.left, key, val)
        tree.height = avl_tree_height(tree)
    else:
        tree.right = avl_insert(tree.right, key, val)
        tree.height = avl_tree_height(tree)

    return avl_self_balance(tree)


def avl_delete(tree: AVLTreeNode, val: Any):
    # base case
    if tree is None:
        return None
    if val < tree.key:
        tree.left = avl_delete(tree.left, val)
    elif val > tree.key:
        tree.right = avl_delete(tree.right, val)
    else:
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left
        replacement = tree_min_node(tree.right)
        replacement.right = avl_delete_min(tree.right)
        replacement.left = tree.left
        tree = replacement
    tree.height = avl_tree_height(tree)
    return avl_self_balance(tree)


def avl_copy(tree):
    if tree is None:
        return None

    new_node = AVLTreeNode(
        tree.key, tree.val,
        left=avl_copy(tree.left),
        right=avl_copy(tree.right)
    )
    new_node.height = tree.height
    return new_node


def tree_equal(tree0: AVLTreeNode, tree1: AVLTreeNode) -> bool:
    if tree0 != tree1:
        return False
    left, right = True, True
    if tree0.left or tree1.left:
        left = tree_equal(tree0.left, tree1.left)
    if tree0.right or tree1.right:
        right = tree_equal(tree0.right, tree1.right)
    return left and right


def tree_complete(tree, idx, count):
    if tree is None:
        return True

    elif idx > count:
        return False

    else:
        return tree_complete(tree.left, 2 * idx, count) \
               and tree_complete(tree.right, 2 * idx + 1, count)


def tree_count(tree):
    if tree is None:
        return 0
    return 1 + tree_count(tree.left) + tree_count(tree.right)


def tree_rank(tree, key):
    if tree is None:
        return 0

    if key < tree.key:
        return tree_rank(tree.left, key)

    elif key > tree.key:
        return 1 + tree_count(tree.left) + tree_rank(tree.right, key)

    else:
        return tree_count(tree.left)


def avl_is_avl(tree):
    if tree is None:
        return True
    if abs(avl_tree_height(tree.left) - avl_tree_height(tree.right)) > 1:
        return False

    return avl_is_avl(tree.left) and avl_is_avl(tree.right)


def avl_ensure_height(tree):
    if tree is None:
        return True
    if tree.height != max(avl_tree_height(tree.left), avl_tree_height(tree.right)) + 1:
        return False
    return avl_ensure_height(tree.left) and avl_ensure_height(tree.right)


class AVLTreeMap:
    def __init__(self, iterable: Dict = None):
        self.tree = None
        if not iterable:
            return

        for k, v in iterable.items():
            self.tree = avl_insert(self.tree, k, v)

    def copy(self):
        new_tree_map = AVLTreeMap()
        new_tree_map.tree = avl_copy(self.tree)
        return new_tree_map

    def __bool__(self):
        return self.tree is not None

    def add(self, key, val):
        self.tree = avl_insert(self.tree, key, val)

    def get(self, key):
        node = tree_get(self.tree, key)
        return node.val

    def rank(self, key):
        return tree_rank(self.tree, key)

    def clear(self):
        self.tree = None

    def __str__(self):
        if self.tree is None:
            return "<empty>"
        return str(self.tree)

    def min(self):
        if self.tree is None:
            raise ValueError()
        return tree_min_node(self.tree).val

    def max(self):
        if self.tree is None:
            raise ValueError()
        return tree_max_node(self.tree).val

    def next_large(self, key):
        n = tree_next_node(self.tree, key)
        if n is None:
            return n
        return n.val

    def prev(self, key):
        n = tree_prev_node(self.tree, key)
        if n is None:
            return n
        return n.val

    def __len__(self):
        return tree_count(self.tree)

    def __eq__(self, other):
        if not isinstance(other, AVLTreeMap):
            return False

        return tree_equal(self.tree, other.tree)

    def delete_min(self):
        minimum = tree_min_node(self.tree)
        self.tree = avl_delete_min(self.tree)
        return minimum if not minimum else minimum.key

    def is_avl(self):
        heights_ok = avl_ensure_height(self.tree)
        if not heights_ok:
            print("failed node height check")
        return heights_ok and avl_is_avl(self.tree)

    def delete_key(self, key):
        self.tree = avl_delete(self.tree, key)
