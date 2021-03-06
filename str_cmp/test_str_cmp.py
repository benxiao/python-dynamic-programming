from unittest import TestCase
from str_cmp import fast_edit_distance, fast_lsc_similarity, fast_hamming_distance


class EditDistanceTests(TestCase):
    def test_basic_function(self):
        self.assertEqual(fast_edit_distance("abc", "fgh"), 5)
        self.assertEqual(fast_edit_distance("maddison", "madison"), 1)

    def test_repeated_character(self):
        self.assertEqual(fast_edit_distance("abbggd", "abbppd"), 1)
        self.assertEqual(fast_edit_distance("abboggle", "abboddle"), 1)
        self.assertEqual(fast_edit_distance("fitzgibbon", "fitzbiggon"), 2)

    def test_adjacent_character_swap(self):
        self.assertEqual(fast_edit_distance("afdfd", "adffd"), 3)
        self.assertEqual(fast_edit_distance("abcdf", "abcfd"), 1)
        self.assertGreater(fast_edit_distance("abc", "bac"), 3)


class LongestCommonSequenceTests(TestCase):
    def test_basic_function(self):
        self.assertEqual(fast_lsc_similarity("abc", "abcd"), 3)

    def test_real_world_examples(self):
        self.assertEqual(fast_lsc_similarity("david smith", "david evan smith"), len("david smith"))


class HammingDistanceTests(TestCase):
    def test_strings_with_same_length(self):
        self.assertEqual(fast_hamming_distance("abc", "adc"), 1)

    def test_strings_with_different_length(self):
        self.assertEqual(fast_hamming_distance("abc", "adcd"), 2)