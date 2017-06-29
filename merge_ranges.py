"""
Given a list of ranges, return a list of ordered ranges
"""


def merge_set(arr):
    """Merge ranges and return in order."""

    arr.sort()
    my_stack = [arr[0]]

    for item in arr[1:]:
        last_range = my_stack[-1]
        first, last = last_range[0], last_range[1]
        if last >= item[0]:
            my_stack.pop()
            my_stack.append((first, max(last, item[1])))
        else:
            my_stack.append(item)

    return my_stack


def test():
    assert merge_set([(1, 5), (3, 6), (7, 8)]) == [(1, 6), (7, 8)]
    assert merge_set([(3, 5), (4, 8), (10, 12), (9, 10), (0, 1)]) == [(0, 1), (3, 8), (9, 12)]
    assert merge_set([(0, 3), (3, 5), (4, 8), (10, 12), (9, 10)]) == [(0, 8), (9, 12)]
    assert merge_set([(0, 3), (3, 5)]) == [(0, 5)]
    assert merge_set([(0, 3), (3, 5), (7, 8)]) == [(0, 5), (7, 8)]
    assert merge_set([(1, 5), (2, 3)]) == [(1, 5)]


test()
