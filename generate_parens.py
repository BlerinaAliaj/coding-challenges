"""
Given a number, generate all possible paranthesis combination
"""


def gen_par(n, left=0, right=0, string=''):
    """Takes a number as an input and generates all possible combintations
    of parenthesis"""

    # When the number of left and right are the same and the right parenthesis
    # number is the same as the input number, return the string
    if left == right and right == n:
        return string

    result = []

    # This generates combinations as long as maximum number has not been reached
    if left < n:
        result.extend(gen_par(n, left + 1, right, string + '('))
    # This generates right parenthesis when left parenthesis has been generated
    if left > right:
        result.extend(gen_par(n, left, right+1, string + ')'))

    return result
