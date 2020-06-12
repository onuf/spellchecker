"""

This module contains tests for distance metrics.

"""


import unittest
from time import time
from distances import levenshtein, recursive_levenshtein


class DistanceTest(unittest.TestCase):

    def test_identical_strings(self):
        """The distance for identical strings should be 0."""

        strings = ("", "cat", "circle", "Levenshtein")
        for s in strings:
            self.assertEqual(levenshtein(s, s), 0)
            self.assertEqual(recursive_levenshtein(s, s), 0)

    def test_empty_source_word(self):
        """The distance from an empty string to the target."""

        self.assertEqual(levenshtein("", "void"), 4)
        self.assertEqual(levenshtein("", "void", ins_cost=2), 8)
        self.assertEqual(levenshtein("", "void", del_cost=3), 4)
        self.assertEqual(levenshtein("", "void", sub_cost=4), 4)
        self.assertEqual(recursive_levenshtein("", "void"), 4)

    def test_empty_target_word(self):
        """The distance from a string to the empty target."""

        self.assertEqual(levenshtein("void", ""), 4)
        self.assertEqual(levenshtein("void", "", del_cost=2), 8)
        self.assertEqual(levenshtein("void", "", ins_cost=3), 4)
        self.assertEqual(levenshtein("void", "", sub_cost=4), 4)
        self.assertEqual(recursive_levenshtein("void", ""), 4)

    def test_deletion(self):
        """Deletion in various positions with varying cost."""

        self.assertEqual(levenshtein("tale", "ale"), 1)
        self.assertEqual(levenshtein("plain", "plan"), 1)
        self.assertEqual(levenshtein("dreams", "dream"), 1)

        self.assertEqual(recursive_levenshtein("tale", "ale"), 1)
        self.assertEqual(recursive_levenshtein("plain", "plan"), 1)
        self.assertEqual(recursive_levenshtein("dreams", "dream"), 1)

        self.assertEqual(levenshtein("trace", "ace"), 2)
        self.assertEqual(levenshtein("oooops", "ops"), 3)

        self.assertEqual(recursive_levenshtein("trace", "ace"), 2)
        self.assertEqual(recursive_levenshtein("oooops", "ops"), 3)

        self.assertEqual(levenshtein("shot", "hot", del_cost=2), 2)
        self.assertEqual(levenshtein("heat", "hat", del_cost=3), 3)
        self.assertEqual(levenshtein("hits", "hit", del_cost=4), 4)
        self.assertEqual(levenshtein("shut", "hut", del_cost=0.5), 0.5)

    def test_insertion(self):
        """Insertion in various positions with varying cost."""

        self.assertEqual(levenshtein("cross", "across"), 1)
        self.assertEqual(levenshtein("tree", "three"), 1)
        self.assertEqual(levenshtein("cheer", "cheers"), 1)

        self.assertEqual(recursive_levenshtein("cross", "across"), 1)
        self.assertEqual(recursive_levenshtein("tree", "three"), 1)
        self.assertEqual(recursive_levenshtein("cheer", "cheers"), 1)

        self.assertEqual(levenshtein("ace", "place"), 2)
        self.assertEqual(levenshtein("L", "XXXL"), 3)

        self.assertEqual(recursive_levenshtein("ace", "place"), 2)
        self.assertEqual(recursive_levenshtein("L", "XXXL"), 3)

        self.assertEqual(levenshtein("ate", "mate", ins_cost=2), 2)
        self.assertEqual(levenshtein("met", "meet", ins_cost=3), 3)
        self.assertEqual(levenshtein("law", "lawn", ins_cost=4), 4)
        self.assertEqual(levenshtein("low", "below", ins_cost=0.5), 1)

    def test_substitution(self):
        """Substitution in various positions with varying cost."""

        self.assertEqual(levenshtein("late", "date"), 2)
        self.assertEqual(levenshtein("tell", "tall"), 2)
        self.assertEqual(levenshtein("pass", "past"), 2)

        self.assertEqual(recursive_levenshtein("glide", "slide"), 2)
        self.assertEqual(recursive_levenshtein("tic", "tac"), 2)
        self.assertEqual(recursive_levenshtein("quite", "quits"), 2)

        self.assertEqual(levenshtein("train", "chain"), 4)
        self.assertEqual(levenshtein("breath", "breeze"), 6)

        self.assertEqual(recursive_levenshtein("ace", "place"), 2)
        self.assertEqual(recursive_levenshtein("L", "XXXL"), 3)

        self.assertEqual(levenshtein("quit", "suit", sub_cost=1), 1)
        self.assertEqual(levenshtein("meet", "meat", sub_cost=2), 2)
        self.assertEqual(levenshtein("look", "loom", sub_cost=0.5), 0.5)
        self.assertEqual(levenshtein("tooth", "teeth", sub_cost=0.5), 1)

    def test_multiple_edits(self):
        """Applying edits of different types."""

        self.assertEqual(levenshtein("kitten", "sitting"), 5)
        self.assertEqual(levenshtein("car", "curse", sub_cost=1), 3)
        self.assertEqual(recursive_levenshtein("intention", "execution"), 8)
        self.assertEqual(recursive_levenshtein("ghost", "mostly"), 5)

    def test_time(self):
        """The recursive implementation is expected to perform slower."""

        start = time()
        x = levenshtein("YPOEHOHRIWUBXMNHZF", "YCPOEHORIDUBXNHZF")
        elapsed = time() - start

        start_rec = time()
        y = recursive_levenshtein("YPOEHOHRIWUBXMNHZF", "YCPOEHORIDUBXNHZF")
        elapsed_rec = time() - start_rec

        self.assertEqual(x, y)
        self.assertLess(elapsed, elapsed_rec)

    def test_hamming(self):
        """The Hamming distance performance test."""

        with self.assertRaises(ValueError):
            hamming("different", "lengths")

        self.assertEqual(hamming("ABC", "ABC"), 0)
        self.assertEqual(hamming("ABc", "ABC"), 1)
        self.assertEqual(hamming("cat", "dog"), 3)
        self.assertEqual(hamming("class", "fleet"), 4)
        self.assertEqual(hamming("taxi", "ixat"), 4)


if __name__ == "__main__":
    unittest.main()
