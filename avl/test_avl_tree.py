import random
from unittest import TestCase

from avl.avl_tree import *

random.seed(0)

N = 2000


class AVLTreeMapTests(TestCase):
    def setUp(self):
        self.keys = list(range(N))
        random.shuffle(self.keys)
        self.tree = AVLTreeMap()
        for k in self.keys:
            self.tree.add(k, k)

        if N <= 30:
            print(end='\n'*3)
            print(self.tree)

    def tearDown(self):
        self.keys = None
        self.tree.clear()

    def testTreeMapAdd(self):
        tree = AVLTreeMap()
        for k in self.keys:
            tree.add(k, k)
            self.assertTrue(tree.is_avl())

        for k in self.keys:
            self.assertEqual(tree.get(k), k)

    def testTreeNodeCount(self):
        self.assertEqual(len(self.tree), len(self.keys))

    def testTreeMin(self):
        self.assertEqual(self.tree.min(), min(self.keys))

    def testTestMax(self):
        self.assertEqual(self.tree.max(), max(self.keys))

    def testNextLarge(self):
        minimum = self.tree.min()
        sorted_keys = sorted(self.keys)
        self.assertEqual(sorted_keys[0], minimum)
        prev = minimum
        for k in sorted_keys[1:]:
            self.assertEqual(self.tree.next_large(prev), k)
            prev = k

    def testDeleteMin(self):
        tree = self.tree.copy()
        sorted_keys = sorted(self.keys, reverse=True)
        while tree:
            self.assertEqual(tree.avl_delete_min(), sorted_keys.pop())
            self.assertTrue(tree.is_avl())

    def testDeleteKey(self):
        tree = self.tree.copy()
        for k in self.keys:
            self.assertEqual(tree.get(k), k)
            tree.delete_key(k)
            self.assertTrue(tree.is_avl())
            with self.assertRaises(KeyError):
                tree.get(k)


    def testTreeRank(self):
        tree = self.tree.copy()
        sorted_keys = sorted(self.keys)
        for i, k in enumerate(sorted_keys):
            self.assertEqual(tree.rank(k), i)







