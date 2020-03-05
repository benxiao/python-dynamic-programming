import random
from unittest import TestCase

from avl.avl_tree import *

random.seed(0)


class AVLTreeMapTests(TestCase):
    def setUp(self):
        self.keys = list(range(30))
        random.shuffle(self.keys)
        self.tree = AVLTreeMap()
        for k in self.keys:
            self.tree.add(k, k)
        print(end='\n' * 4)
        print(self.tree)

    def testTreeMapAdd(self):
        tree = AVLTreeMap()
        for k in self.keys:
            tree.add(k, k)
            self.assertTrue(tree.is_avl())

        for k in self.keys:
            self.assertEqual(tree.get(k), k)


