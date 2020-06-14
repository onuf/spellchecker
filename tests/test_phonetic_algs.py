"""

Tests for phonetic algorithms.

"""


import unittest
from phonetic_algs import soundex


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


if __name__ == "__main__":
    unittest.main()
