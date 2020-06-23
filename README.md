Spelling correction has become a typical task as people write more and more texts daily. Some took to this feature of text processing tools to the point of not daring to use them without it. Spell checks have made their way to lots of programs, from email clients to search engines and virtual keyboards. That's why it might be interesting to find out how all of this works.

### Spelling correction in a nutshell

We can break down spell checking into two main subtasks: error detection and error correction. The correction part may take on different forms, from simple autocorrect to one or more pop-up suggestions. The course of actions often depends on a system's confidence or established policies.

In spelling error detection, there are two types of errors:

- *NWEs*, or *non-word errors*, 
- *RWEs*, or *real-word errors*.

The former are not real words of language, e.g., *google* instead of *googol*, *fime* instead of *fame*, *fire*, or *dime*. The real-word errors, as the name suggests, are valid words used in the wrong context, when some other word was implied, for example, *to-too-two*, *piece-peace*, *three-tree*. Some mistakes of this type are trivial typing errors, but most of them appear to be cognitive errors, which stem from similar pronunciation. Words that sound the same are called *homophones*. Phonetic algorithms are better-equipped to detect them.

Non-words are easier to detect: we simply check if a word is in our dictionary. For real words, we should assume that each word might be an error and pick the candidate corrections that maximize the probability of the whole sentence. Though in practice, it boils down to an assumption that only *n* words per sentence are misused, thus, we suggest only *n* corrections.

When generating candidates, we search for real words that have similar spelling and/or pronunciation and form a set of candidates. That's where we choose the best correction(s) from.

### Contents

Modules:
- [distances.py](https://github.com/onuf/spellchecker/blob/master/distances.py) contains distances between two strings, which are useful to catch misprints and typing errors (orthography).
- [phonetic_algs.py](https://github.com/onuf/spellchecker/blob/master/phonetic_algs.py) includes phonetic algorithms, which help deal with cognitive errors and homophones (pronunciation).
- [spellchecker.ipynb](https://github.com/onuf/spellchecker/blob/master/spellchecker.ipynb) -- a Jupyter Notebook with explanations.

### Things to try

- Train a classifier to distinguish between the varieties of English (American, Australian, British, Canadian, etc.), which can ensure consistency in spelling. Given a solid piece of text, you can decide on a subset of dictionary to refer to.
- Improve the error model. In practice, some letters are more likely to be mistyped than others. See this [confusion matrix](https://web.stanford.edu/class/cs124/lec/spelling.pdf#page=22). For example, vowels often tend to be confused. The keybord layout appears to have an impact as well. Plus, there might be a research somewhere on typical misspellings made by dyslexic people. All these things can be used for model development.
- Work on the noisy channel model: the language model or the channel model might have very different ranges. An additional parameter may solve the problem.
- Implement other phonetic algorithms or Jaro-Winkler distance.
- DL for spelling correction.

### Useful links

- [The Spelling Correction Task from an NLP course by Dan Jurafsky and Chris Manning](https://youtu.be/tD3Fp-dc0gs)
- [Speech and Language Processing (3rd ed. draft), Appendix B. 	Spelling Correction and the Noisy Channel](https://web.stanford.edu/~jurafsky/slp3/B.pdf)
- [How to Write a Spelling Corrector by Peter Norvig](https://norvig.com/spell-correct.html)
