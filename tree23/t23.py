from typing import *


class SingleNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def is_leave(self):
        return (not self.left) and (not self.right)

    def __str__(self):
        return f"S[{self.key}]({self.left}, {self.right})"


class DoubleNode:
    def __init__(self, left_key, right_key,
                 left=None, middle=None, right=None):
        self.left_key = left_key
        self.right_key = right_key
        self.left = left
        self.middle = middle
        self.right = right

    def is_leave(self):
        return (not self.left) and (not self.middle) and (not self.right)

    def __str__(self):
        return f"D[{(self.left_key, self.right_key)}]({self.left}, {self.middle}, {self.right})"


class TripleNode:
    def __init__(self, left_key, middle_key, right_key,
                 most_left=None, left=None, right=None, most_right=None):
        self.left_key = left_key
        self.right_key = right_key
        self.middle_key = middle_key
        self.most_left = most_left
        self.left = left
        self.right = right
        self.most_right = most_right

    def is_leave(self):
        return (not self.most_left) and (not self.left) and (not self.right) and (not self.most_right)


def r_exists(tree: Union[SingleNode, DoubleNode, None], key) -> bool:
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


def r_insert(tree: Union[SingleNode, DoubleNode, TripleNode], key) -> Union[SingleNode, DoubleNode, TripleNode]:
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

                    new_left = SingleNode(left_subtree.left_key,
                                          left=left_subtree.most_left,
                                          right=left_subtree.left)

                    new_middle = SingleNode(left_subtree.right_key,
                                            left=left_subtree.right,
                                            right=left_subtree.most_right)
                    ####
                    new_node = DoubleNode(left_subtree.middle_key, tree.key,
                                          left=new_left,
                                          middle=new_middle,
                                          right=tree.right)
                    return new_node
                else:
                    tree.left = left_subtree
                    return tree
            else:
                right_subtree = r_insert(tree.right, key)
                if isinstance(right_subtree, TripleNode):
                    ####

                    new_right = SingleNode(right_subtree.right_key,
                                           left=right_subtree.right,
                                           right=right_subtree.most_right)
                    new_middle = SingleNode(right_subtree.left_key,
                                            left=right_subtree.most_left,
                                            right=right_subtree.left
                                            )
                    new_node = DoubleNode(tree.key, right_subtree.middle_key,
                                          left=tree.left,
                                          middle=new_middle,
                                          right=new_right)
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
                    new_most_left = SingleNode(left_subtree.left_key,
                                               left=left_subtree.most_left,
                                               right=left_subtree.left)
                    new_left = SingleNode(left_subtree.right_key,
                                          left=left_subtree.right,
                                          right=left_subtree.most_right)

                    new_node = TripleNode(left_subtree.middle_key, tree.left_key, tree.right_key,
                                          most_left=new_most_left,
                                          left=new_left,
                                          right=tree.middle,
                                          most_right=tree.right)
                    return new_node
                else:
                    tree.left = left_subtree
                    return tree
            elif key > tree.right_key:
                right_subtree = r_insert(tree.right, key)
                if isinstance(right_subtree, TripleNode):
                    new_right = SingleNode(right_subtree.left_key,
                                           left=right_subtree.most_left,
                                           right=right_subtree.left)
                    new_most_right = SingleNode(right_subtree.right_key,
                                                left=right_subtree.right,
                                                right=right_subtree.most_right)

                    new_node = TripleNode(tree.left_key, tree.right_key, right_subtree.middle_key,
                                          most_left=tree.left,
                                          left=tree.middle,
                                          right=new_right,
                                          most_right=new_most_right)
                    return new_node
                else:
                    tree.right = right_subtree
                    return tree

            else:
                middle_subtree = r_insert(tree.middle, key)
                if isinstance(middle_subtree, TripleNode):
                    new_left = SingleNode(middle_subtree.left_key,
                                          left=middle_subtree.most_left,
                                          right=middle_subtree.left)
                    new_right = SingleNode(middle_subtree.right_key,
                                           left=middle_subtree.right,
                                           right=middle_subtree.most_right)

                    new_node = TripleNode(tree.left_key, middle_subtree.middle_key, tree.right_key,
                                          most_left=tree.left,
                                          left=new_left,
                                          right=new_right,
                                          most_right=tree.right)
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

            new_left = SingleNode(tree.left_key,
                                  left=tree.most_left,
                                  right=tree.left)
            
            new_right = SingleNode(tree.right_key,
                                   left=tree.right,
                                   right=tree.most_right)

            new_node = SingleNode(tree.middle_key,
                                  left=new_left,
                                  right=new_right)
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


