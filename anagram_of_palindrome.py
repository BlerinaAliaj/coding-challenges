"""
Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards (eg, 'racecar', 'tacocat').
An anagram is a rescrambling of a word (eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.

The word will only contain lowercase letters, a-z.

"""


def is_anagram_of_palindrome(word):
    """Returns true if if is anagram of palindrome

        >>> is_anagram_of_palindrome("a")
        True

        >>> is_anagram_of_palindrome("ab")
        False

        >>> is_anagram_of_palindrome("aab")
        True

        >>> is_anagram_of_palindrome("arceace")
        True

        >>> is_anagram_of_palindrome("arceaceb")
        False

        >>> is_anagram_of_palindrome("tattarrattat")
        True


    """

    my_dict = {}
    count = 0

    for let in word:
        my_dict[let] = my_dict.get(let, 0) + 1

    for key in my_dict:
        if my_dict[key] < 2:
            count += 1

    return count < 2


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
