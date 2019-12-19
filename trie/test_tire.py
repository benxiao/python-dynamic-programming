from unittest import TestCase
import random

random.seed(0)

from trie import Trie


class TestTire(TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add("David")
        self.trie.add("David")
        self.trie.add("Dave")
        self.trie.add("Davidson")

    def test_recall(self):
        self.assertEqual(self.trie.count("David"), 2)
        self.assertEqual(self.trie.overlay_count("David"), 3)
        with self.assertRaises(KeyError):
            self.trie.count("Ben")

    def test_exists(self):
        self.assertFalse(self.trie.exist("Davison"))
        self.assertTrue(self.trie.exist("David"))
        self.assertFalse(self.trie.exist("Dav"))

    def test_initializer(self):
        trie = Trie(["David", "David", "Dave", "Davidson"])
        self.assertEqual(trie.count("David"), 2)
        self.assertEqual(trie.overlay_count("David"), 3)

    def test_random(self):
        name, count = self.trie.random()
        self.assertEqual(type(name), str)
        self.assertEqual(type(count), int)



