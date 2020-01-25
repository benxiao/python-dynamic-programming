from typing import *


class SingleNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def is_leave(self):
        return (not self.left) and (not self.right)

    def __str__(self):
        return f"S[{self.key}]({self.left}, {self.right})"


class DoubleNode:
    def __init__(self, left_key, right_key):
        self.left_key = left_key
        self.right_key = right_key
        self.left = None
        self.middle = None
        self.right = None

    def is_leave(self):
        return (not self.left) and (not self.middle) and (not self.right)

    def __str__(self):
        return f"D[{(self.left_key, self.right_key)}]({self.left}, {self.middle}, {self.right})"


class TripleNode:
    def __init__(self, left_key, middle_key, right_key):
        self.left_key = left_key
        self.right_key = right_key
        self.middle_key = middle_key
        self.most_left = None
        self.left = None
        self.right = None
        self.most_right = None

    def is_leave(self):
        return (not self.most_left) and (not self.left) and (not self.right) and (not self.most_right)


def r_exists(tree:Union[SingleNode, DoubleNode, None], key) -> bool:
    if tree is None:
        return False
    if isinstance(tree, SingleNode):
        if key < tree.key:
            return r_exists(tree.left, key)
        elif key > tree.key:
            return r_exists(tree.right, key)
    elif isinstance(tree, DoubleNode):
        if key < tree.left_key:
            return r_exists(tree.left, key)
        elif tree.left_key < key < tree.right_key:
            return r_exists(tree.middle, key)
        elif key > tree.right_key:
            return r_exists(tree.right, key)
    return True


def r_insert(tree: Union[SingleNode, DoubleNode, TripleNode], key)->Union[SingleNode, DoubleNode, TripleNode]:
    if tree is None:
        return SingleNode(key)

    elif isinstance(tree, SingleNode):
        if tree.is_leave():
            left_key, right_key = key, tree.key
            if left_key > right_key:
                left_key, right_key = right_key, left_key
            return DoubleNode(left_key, right_key)
        else:
            if key < tree.key:
                left_subtree = r_insert(tree.left, key)
                if isinstance(left_subtree, TripleNode):
                    ####
                    new_node = DoubleNode(left_subtree.middle_key, tree.key)
                    new_node.left = SingleNode(left_subtree.left_key)
                    new_node.middle = SingleNode(left_subtree.right_key)
                    ####
                    new_node.left.left = left_subtree.most_left
                    new_node.left.right = left_subtree.left
                    new_node.middle.left = left_subtree.right
                    new_node.middle.right = left_subtree.most_right
                    new_node.right = tree.right
                    return new_node
                else:
                    tree.left = left_subtree
                    return tree
            else:
                right_subtree = r_insert(tree.right, key)
                if isinstance(right_subtree, TripleNode):
                    ####
                    new_node = DoubleNode(tree.key, right_subtree.middle_key)
                    new_node.right = SingleNode(right_subtree.right_key)
                    new_node.middle = SingleNode(right_subtree.left_key)
                    ####
                    new_node.right.right = right_subtree.most_right
                    new_node.right.left = right_subtree.right
                    new_node.middle.left = right_subtree.most_left
                    new_node.middle.right = right_subtree.left
                    new_node.left = tree.left
                    return new_node
                else:
                    tree.right = right_subtree
                    return tree

    elif isinstance(tree, DoubleNode):
        if tree.is_leave():
            if key < tree.left_key:
                return TripleNode(key, tree.left_key, tree.right_key)
            elif key > tree.right_key:
                return TripleNode(tree.left_key, tree.right_key, key)
            else:
                return TripleNode(tree.left_key, key, tree.right_key)
        else:
            if key < tree.left_key:
                left_subtree = r_insert(tree.left, key)
                if isinstance(left_subtree, TripleNode):
                    new_node = TripleNode(left_subtree.middle_key, tree.left_key, tree.right_key)
                    new_node.most_left = SingleNode(left_subtree.left_key)
                    new_node.left = SingleNode(left_subtree.right_key)
                    new_node.most_left.left = left_subtree.most_left
                    new_node.most_left.right = left_subtree.left
                    new_node.left.left = left_subtree.right
                    new_node.left.right = left_subtree.most_right
                    new_node.right = tree.middle
                    new_node.most_right = tree.right
                    return new_node
                else:
                    tree.left = left_subtree
                    return tree
            elif key > tree.right_key:
                right_subtree = r_insert(tree.right, key)
                if isinstance(right_subtree, TripleNode):
                    new_node = TripleNode(tree.left_key, tree.right_key, right_subtree.middle_key)
                    new_node.right = SingleNode(right_subtree.left_key)
                    new_node.most_right = SingleNode(right_subtree.right_key)
                    new_node.right.left = right_subtree.most_left
                    new_node.right.right = right_subtree.left
                    new_node.most_right.left = right_subtree.right
                    new_node.most_right.right = right_subtree.most_right
                    new_node.most_left = tree.left
                    new_node.left = tree.middle
                    return new_node
                else:
                    tree.right = right_subtree
                    return tree

            else:
                middle_subtree = r_insert(tree.middle, key)
                if isinstance(middle_subtree, TripleNode):
                    new_node = TripleNode(tree.left_key, middle_subtree.middle_key, tree.right_key)
                    new_node.left = SingleNode(middle_subtree.left_key)
                    new_node.right = SingleNode(middle_subtree.right_key)
                    new_node.left.left = middle_subtree.most_left
                    new_node.left.right = middle_subtree.left
                    new_node.right.left = middle_subtree.right
                    new_node.right.right = middle_subtree.most_right
                    new_node.most_left = middle_subtree.most_left
                    new_node.most_right = middle_subtree.most_right
                    return new_node
                else:
                    tree.middle = middle_subtree
                    return tree


class Tree23:
    def __init__(self):
        self.tree: Union[SingleNode, DoubleNode, None] = None

    def insert(self, key):
        tree = r_insert(self.tree, key)
        if isinstance(tree, TripleNode):
            new_node = SingleNode(tree.middle_key)
            new_node.left = SingleNode(tree.left_key)
            new_node.right = SingleNode(tree.right_key)
            new_node.left.left = tree.most_left
            new_node.left.right = tree.left
            new_node.right.left = tree.right
            new_node.right.right = tree.most_right
            self.tree = new_node
        else:
            self.tree = tree

    def __str__(self):
        if self.tree:
            return str(self.tree)
        return "<empty_tree>"

    def exists(self, key):
        return r_exists(self.tree, key)


if __name__ == '__main__':
    tree = Tree23()
    tree.insert(50)
    print(tree)
    tree.insert(60)
    print(tree)
    tree.insert(70)
    print(tree)
    tree.insert(30)
    print(tree)
    tree.insert(40)
    print(tree)
    tree.insert(20)
    print(tree)
    tree.insert(10)
    print(tree)

    print(tree.exists(10))
    print(tree.exists(100))


