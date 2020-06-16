"""

Tests for phonetic algorithms.

"""


import unittest
from phonetic_algs import soundex
from distances import levenshtein


class SoundexTest(unittest.TestCase):

    def test_empty_s(self):
        """Index an empty string."""

        self.assertEqual(soundex(""), "0000")

    def test_vowels(self):
        """Test strings starting with the first group *aeiouyhw*."""

        self.assertEqual(soundex("AI"), "A000")
        self.assertEqual(soundex("you"), "Y000")
        self.assertEqual(soundex("either"), "E360")
        self.assertEqual(soundex("and"), "A530")
        self.assertEqual(soundex("ammonium"), "A555")
        self.assertEqual(soundex("Ashcraft"), "A261")
        self.assertEqual(soundex("Ashcroft"), "A261")
        self.assertEqual(soundex("Honeyman"), "H555")

    def test_consonants(self):
        """Test names starting with consonants."""

        self.assertEqual(soundex("Robert"), "R163")
        self.assertEqual(soundex("Robert"), soundex("Rupert"))
        self.assertEqual(soundex("Rubin"), "R150")
        self.assertEqual(soundex("Tymczak"), "T522")
        self.assertEqual(soundex("Pfister"), "P236")

    def test_levenshtein(self):
        """
        For certain types of errors, Levenshtein edit distance between words'
        spellings is greater than the distance between their Soundex indices.
        """

        sent1 = 'PLEZ CNOKE IF AN RNSR IS NOT REQID'
        toks1 = sent1.lower().split()
        sent2 = 'Please knock if an answer is not required'
        toks2 = sent2.lower().split()
        total = sum(levenshtein(*pair) for pair in zip(toks1, toks2))
        sndx_total = sum(levenshtein(soundex(pair[0]), soundex(pair[1]))
                         for pair in zip(toks1, toks2))
        self.assertGreater(total, sndx_total)

        homophones = (('tail', 'tale'), ('right', 'write'),
                      ('flower', 'flour'), ('break', 'brake'),
                      ('accept', 'except'), ('you\'re', 'your'))
        total2 = sum(levenshtein(*pair, sub_cost=1) for pair in homophones)
        sndx_total2 = sum(levenshtein(soundex(pair[0]), soundex(pair[1]))
                          for pair in homophones)
        self.assertGreaterEqual(total2, sndx_total2)


if __name__ == "__main__":
    unittest.main()
