from enum import Enum
from colorama import Fore
import re

class RBTreeNodeColor:
    Red = 0
    Black = 1


def rb_color(tree):
    if tree is None:
        return RBTreeNodeColor.Black
    return tree.color


class RBTreeNode:
    def __init__(self, key, val, color=None, left=None, right=None):
        self.key = key
        self.val = val
        self.color = color or RBTreeNodeColor.Red
        self.left = left
        self.right = right

    def __str__(self):
        if self is None:
            return '<empty tree>'

        def recurse(node):
            if node is None:
                return [], 0, 0

            label = f"({node.color}:{node.key})"

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
            if label[0] == '.':
                label = ' ' + label[1:]
            if label[-1] == '.':
                label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        ascii_art = '\n'.join(recurse(self)[0])
        ascii_art = re.sub(r"(\(0:.*\))", rf"{Fore.RED}\1{Fore.RESET}", ascii_art)
        ascii_art = re.sub(r"(\(1:.*\))", rf"{Fore.GREEN}\1{Fore.RESET}", ascii_art)
        return ascii_art


def rb_invariants_check(tree):
    """
    1. Every node is either red or black. (only two colors allowed)
    2. The root is black.
    3. Every leaf (NIL) is black. (enforced in code)
    4. If a node is red, then both its children are black.
    5. For each node, all simple paths from the node to descendant leaves contain the same

    """
    # check 1
    if tree.color is not RBTreeNodeColor.Black:
        return False

    # check 4
    if not red_parent_should_not_have_red_child(tree):
        return False

    # check 5
    if not same_black_count_on_all_path(tree):
        return False

    return True


def same_black_count_on_all_path(tree):
    if tree is None:
        return 0, True

    lc, lt = same_black_count_on_all_path(tree.left)
    rc, rt = same_black_count_on_all_path(tree.right)
    if (not lt) or (not rt):
        return -1, False

    if lc == rc:
        return (1 if tree.color is RBTreeNodeColor.Black else 0) + lc, True

    return -1, False


def red_parent_should_not_have_red_child(tree):
    if tree is None:
        return True
    if tree.color is RBTreeNodeColor.Red and \
            ((rb_color(tree.left) is RBTreeNodeColor.Red) or (rb_color(tree.right) is RBTreeNodeColor.Red)):
        return False

    return red_parent_should_not_have_red_child(tree.left) and red_parent_should_not_have_red_child(tree.right)


if __name__ == '__main__':
    root = RBTreeNode(3, 3, color=RBTreeNodeColor.Black,
                      left=RBTreeNode(1, 1),
                      right=RBTreeNode(5,5))
    print(root)
