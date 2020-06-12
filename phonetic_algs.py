"""

Phonetic algorithms for English.
As opposed to edit distances, phonetic algorithms offer a means
to compare words by their pronunciation rather than spelling.
The rules largely depend on the phonological system of a given
language and, therefore, are language-specific.

"""


from string import ascii_letters


def soundex(s, /):
    """
    An implementation of the phonetic algorithm Soundex.

    Letters are grouped into the following clusters:
      aeiouyhw    0
      bfpv        1
      cgjkqsxz    2
      dt          3
      l           4
      mn          5
      r           6
    The first group, which mainly consists of English vowels (+ yhw),
    is discarded in the course of indexing the input text by sound.

    Positional-only params:
      s: a string to encode.

    Returns:
      A four-character alphanumeric sequence in the format {X123}.
      It starts at a single letter followed by three digits, with
      the only exception for an empty input string {0000}. Also,
      the output will be padded with trailing 0s if it's too short.
    """

    if not s:
        return "0000"

    # Keep only ASCII letters and switch them to upper case
    s = "".join(char.upper() for char in s if char in ascii_letters)
    # Add the first letter
    sndx = s[0]

    codes = {'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '0', 'F': '1',
             'G': '2', 'H': '0', 'I': '0', 'J': '2', 'K': '2', 'L': '4',
             'M': '5', 'N': '5', 'O': '0', 'P': '1', 'Q': '2', 'R': '6',
             'S': '2', 'T': '3', 'U': '0', 'V': '1', 'W': '0', 'X': '2',
             'Y': '0', 'Z': '2'}

    # Replace all letters (the first one included) with digits
    sndx += "".join(codes[char] for char in s)

    # Replace adjacent identical consonants
    sndx = sndx[:2] + "".join(char for i, char in enumerate(sndx[2:], start=2)
                              if char != sndx[i-1])

    # Remove coded vowels and pad the string with trailing zeros
    sndx = sndx.replace("0", "") + "0000"

    # Remove the first digit if it corresponds to the first letter
    if codes[sndx[0]] == sndx[1]:
        sndx = sndx[0] + sndx[2:]

    return sndx[:4]
