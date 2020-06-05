"""

Functions from this module can be used to measure lexical word similarity.
Lexical similarity indicates how close the surface word forms are.
The meanings of the words as such are not compared in any way.

"""


from functools import lru_cache


def levenshtein(x, y, /, *, del_cost=1, ins_cost=1, sub_cost=2):
    """
    The function computes the Levenshtein distance between strings x and y.

    The Levenshtein algorithm is used to calculate the distance between
    two words as the minimum number of single-character edits (deletions,
    insertions, substitutions) required to transform one word into another.

    Every edit comes at a cost: 1 for each deleted or inserted character,
    2 for every substitution. The last cost is higher by default since
    substitution can be viewed as the combination of deletion and insertion.

    Examples:
      "tale" > "ale":         1 (deletion)
      "tree" > "three":       1 (insertion)
      "cell" > "hell":        2 (substitution)
      "kitten" > "sitting":   5 (two substitutions and one insertion)

    Positional-only params:
      x: a string to be transformed (the initial word).
      y: a string to transform into (the target word).

    Keyword-only params:
      del_cost: the cost of deletion.
      ins_cost: the cost of insertion.
      sub_cost: the cost of substitution.

    Returns:
      An (integer) number of edits describing the shortest path from x to y.
    """

    # The initial check if strings are identical
    if x == y:
        return 0

    n = len(x)
    m = len(y)

    # Delete all chars of x to match empty y: D(n, 0) = n
    if not m:
        return n * del_cost

    # Insert all chars of y into the empty x: D(0, m) = m
    if not n:
        return m * ins_cost

    # We work only with two rows of the matrix D at a time:
    # D = [[0 for j in range(m+1)] for i in range(n+1)]

    # At the start, the previous row contains the edit distance for
    # y's prefixes and empty x (the number of chars to insert into x)
    prev_row = [i * ins_cost for i in range(m + 1)]

    cur_row = [0 for _ in range(m + 1)]

    # Comlete the current row
    for i in range(n):
        # The 1st element is the edit distance for x and empty y.
        # It's the number of chars to delete from x to match y.
        cur_row[0] = i + del_cost

        for j in range(m):
            del_ = prev_row[j + 1] + del_cost
            ins = cur_row[j] + ins_cost
            sub = prev_row[j]

            # If chars are the same, there is no substitution.
            # Otherwise, we add the cost of this operation.
            if x[i] != y[j]:
                sub += sub_cost

            cur_row[j + 1] = min(del_, ins, sub)

        # Update the previous row
        prev_row = cur_row[:]

    return prev_row[-1]


@lru_cache(maxsize=None)
def recursive_levenshtein(x, y, /):
    """
    A recursive implementation of the Levenshtein distance.
    Whenever possible, use the alternative function instead.
    Multiple recomputations typical of recursive functions
    are avoided here by means of recent call caching. Still,
    this gain in time makes the function unresponsive to
    on-the-fly adjustments of edit costs (so there aren't any).

    See details on Levenshtein distance in the function `levenshtein`.

    Positional-only params:
      x: a string to be transformed (the initial word).
      y: a string to transform into (the target word).

    Returns:
      An integer number of edits describing the shortest path from x to y.
    """

    # The operation costs
    cost = {"del": 1, "ins": 1, "sub": 2}

    # The initial check if strings are identical
    if x == y:
        return 0

    n = len(x)
    m = len(y)

    # Delete all chars of x to match empty y: D(n, 0) = n
    if not m:
        return n * cost["del"]

    # Insert all chars of y into the empty x: D(0, m) = m
    if not n:
        return m * cost["ins"]

    # Recurrence relation
    del_ = recursive_levenshtein(x[:-1], y) + cost["del"]
    ins = recursive_levenshtein(x, y[:-1]) + cost["ins"]
    sub = recursive_levenshtein(x[:-1], y[:-1])

    # If chars are the same, technically, there is no substitution.
    # Otherwise, we should add the cost of this operation.
    if x[-1] != y[-1]:
        sub += cost["sub"]

    return min(del_, ins, sub)
