from typing import *


class Node:
    def __init__(self, key):
        self.count = 1
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.key}({self.left},{self.right})"


def tree_insert(tree, key):
    if not tree:
        return Node(key)
    if key < tree.key:
        tree.left = tree_insert(tree.left, key)
        tree.count = tree_size(tree.left) + 1 + tree_size(tree.right)
    else:
        tree.right = tree_insert(tree.right, key)
        tree.count = tree_size(tree.left) + 1 + tree_size(tree.right)
    return tree


def tree_floor(tree, key):
    if not tree:
        return None
    if key == tree.key:
        return tree
    elif key < tree.key:
        return tree_floor(tree.left, key)
    t = tree_floor(tree.right, key)
    if t:
        return t
    else:
        return tree


def tree_ceil(tree, key):
    if not tree:
        return None
    if key == tree.key:
        return tree
    elif key > tree.key:
        return tree_ceil(tree.right, key)
    t = tree_ceil(tree.left, key)
    if t:
        return t
    else:
        return tree


def tree_search(tree, key):
    if not tree:
        return None
    if key < tree.key:
        return tree_search(tree.left, key)
    elif key > tree.key:
        return tree_search(tree.right, key)
    return tree


def tree_size(tree):
    return tree.count if tree else 0


def tree_rank(tree, key):
    if not tree:
        return 0
    if key < tree.key:
        return tree_rank(tree.left, key)
    elif key > tree.key:
        return 1 + tree_size(tree.left) + tree_rank(tree.right, key)
    else:
        return tree_size(tree.left)


def tree_delete(tree, key):
    if not tree:
        return None
    if key < tree.key:
        tree.left = tree_delete(tree, key)
        # do we need to change count here?
    elif key > tree.key:
        tree.right = tree_delete(tree, key)
    else:
        if not tree.left:
            return tree.right
        elif not tree.right:
            return tree.left
        next_in_line = tree_min(tree.right)
        right = tree_delete_min(tree.right)
        tree = next_in_line
        tree.right = right
        tree.left = tree.left
    tree.count = tree_size(tree.left) + tree_size(tree.right) + 1
    return tree


def tree_height(tree):
    if not tree:
        return 0
    left = tree_height(tree.left)
    right = tree_height(tree.right)
    return 1 + max(left, right)


def tree_min(tree):
    if not tree:
        return None
    if tree.left:
        return tree_min(tree.left)
    return tree


def tree_delete_min(tree):
    if not tree:
        return None

    if not tree.left:
        return tree.right

    tree.left = tree_delete_min(tree.left)
    tree.count = tree_size(tree.left) + tree_size(tree.right) + 1
    return tree


def perfect_balanced_insertion_sequence(keys, l, r):
    if r < l:
        return []
    if r == l:
        return [l]
    mid = (r+l) // 2
    return [mid, *perfect_balanced_insertion_sequence(keys, l, mid - 1),
            *perfect_balanced_insertion_sequence(keys, mid + 1, r)]


def tree_str(tree):
    if tree is None: return '<empty tree>'
    def recurse(node):
        if node is None: return [], 0, 0
        label = str(node.key)
        left_lines, left_pos, left_width = recurse(node.left)
        right_lines, right_pos, right_width = recurse(node.right)
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        # put a empty space at front when it starts with a 'dot'
        if label[0] == '.': label = ' ' + label[1:]
        # put a empty space at the end
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle - 2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) +
                 right_line
                 for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width
    return '\n'.join(recurse(tree)[0])


class Tree:
    def __init__(self):
        self.tree: Union[None, Node] = None

    def __len__(self):
        return self.tree.count

    def search(self, key):
        return tree_search(self.tree, key)

    def insert(self, key):
        self.tree = tree_insert(self.tree, key)

    def rank(self, key):
        return tree_rank(self.tree, key)

    def floor(self,key):
        return tree_floor(self.tree, key)

    def ceil(self, key):
        return tree_ceil(self.tree, key)

    def min(self):
        return tree_min(self.tree)

    def delete(self, key):
        self.tree = tree_delete(self.tree, key)

    def height(self):
        return tree_height(self.tree)

    def __str__(self):
        return tree_str(self.tree)


if __name__ == '__main__':
    t = Tree()
    t.insert("E")
    t.insert("C")
    t.insert("A")
    t.insert("D")
    t.insert("K")
    t.insert("I")
    t.insert("Z")
    print(t.tree)
    print(t.rank('A'))
    print(t.rank('C'))
    print(t.floor("B"))
    print(t.ceil("B"))
    t.delete("E")
    print(t)
    t2 = Tree()
    idxes = perfect_balanced_insertion_sequence(list(range(15)), 0, 14)
    for i in idxes:
        t2.insert(i)

    print(t2)


    print(perfect_balanced_insertion_sequence(list(range(10)), 0, 9))