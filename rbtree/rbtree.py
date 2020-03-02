from enum import Enum


class RBTreeNodeColor:
    Red=0
    Black=1


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

    return red_parent_should_not_have_red_child(tree.left) and \
           red_parent_should_not_have_red_child(tree.right)






if __name__ == '__main__':
    pass