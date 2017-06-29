"""
Imagine there's a lemming currenly in each hole, and they're all hungry.
The lemmings in hole #3 and #5 don't need to travel at all, but the other lemmings
need to travel to find the nearest cafe:

the lemming in hole #1 needs to travel 2m to hole #3
the lemming in hole #2 needs to travel 1m to hole #3
the lemming in hole #4 needs to travel 1m to hole #3 (or 1m to hole #5)
the lemming in hole #6 needs to travel 1m to hole #5
In this problem, you want to calculate the longest amount, in meters, any lemming
needs to travel to get food. For this example, the answer would 2, since lemming
in hole #1 needs to travel 2m to get to the nearest cafe.
"""


def longest_travel(num_holes, cafes):
    """Returns true if if is anagram of palindrome

        >>> longest_travel(6, [2, 4])
        2
        >>> longest_travel(11, [0, 4, 10])
        3

    """

    distances = [cafes[0], num_holes-1 - cafes[-1]]

    for i in range(1, len(cafes)):
        distances.append((cafes[i] - cafes[i-1]) / 2)

    return max(distances)


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print